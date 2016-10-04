from django.test import TestCase
from accounts.models import Event, Wallet, AccountStatus, Transactions, Sale, PersonalAccount
from inscription.models import Affiliate, Scout
from datetime import date


class AccountTestCase(TestCase):
    def setUp(self):
        self.now = date.today()
        self.cantidad_de_cuentas = AccountStatus.objects.count()
        self.cantidad_de_wallets = Wallet.objects.count()
        self.cantidad_de_transactions = Transactions.objects.count()
        self.new_event = Event.objects.create(name='nombre_del_evento',description='descripcion_del_evento',start=self.now)
        self.new_affiliate = Scout.objects.create(name='nombre_del_afiliado', dni=122334254, birthday=self.now, phone=123123123, adress='la_direccion', email='el_email@exp.com')
        self.new_account = AccountStatus.objects.last()
        self.new_wallet = Wallet.objects.last()
        last_personal_accounts = PersonalAccount.objects.last()
        self.last_personal_accounts_amount = last_personal_accounts.amount
        self.new_sale = Sale.objects.create(name='ventalocro',seller=last_personal_accounts, event=self.new_event, amount=10 , quantity=5)
        #self.new_account = AccountStatus.objects.create(name='nombre_de_la_cuenta',start=self.now)
        #self.new_wallet = Wallet.objects.create(name="la wallet", creation=self.now, amount=0)

    def test_after_event_creation_account_is_created(self):
        self.assertEqual(AccountStatus.objects.count(), self.cantidad_de_cuentas+1)
        last_account = AccountStatus.objects.last()
        self.assertEqual(last_account.name, self.new_event.name+"_"+str(self.new_event.start))
        self.assertEqual(last_account.start, self.new_event.start)
        self.assertEqual(last_account.close, self.new_event.close)

    def test_after_account_creation_wallet_is_created(self):
        self.assertEqual(Wallet.objects.count(), self.cantidad_de_wallets+1)
        last_wallet = Wallet.objects.last()
        self.assertEqual(last_wallet.creation, self.new_account.start)
        self.assertEqual(last_wallet.name, self.new_account.name + "_wallet")
        self.assertEqual(self.new_account.wallet, last_wallet)

    def test_close_account_status(self):
        new_account = AccountStatus.objects.create(name='nombre_de_la_cuenta_test_cierre',start=date.today())
        account_closed = new_account.close_account()
        self.assertTrue(account_closed)
        self.assertEqual(new_account.close, date.today())

    def test_get_balances(self):
        new_account = self.new_account
        account_wallet = new_account.wallet
        first_transaction = Transactions.objects.create(destination=account_wallet, description="Primera transaccion", date=date.today(), amount=1000)
        second_transaction = Transactions.objects.create(destination=account_wallet, description="Segunda transaccion", date=date.today(), amount=-500)
        self.assertFalse(new_account.get_account_balance())
        new_account.close_account()
        current_account_balance = new_account.get_account_balance()
        account_movements = self.new_sale.amount * self.new_sale.quantity + first_transaction.amount + second_transaction.amount
        self.assertEqual(current_account_balance, account_movements)

    def test_after_sale_creation_transactions_is_created(self):
        last_personal_accounts =  self.new_sale.seller
        transaction_wallet = Wallet.objects.get(name = self.new_sale.event.name + "_" + str(self.new_sale.event.start) + "_wallet")
        self.assertEqual(Transactions.objects.count(), self.cantidad_de_transactions+1)
        last_tansactions = Transactions.objects.last()
        self.assertEqual(last_tansactions.amount, self.new_sale.amount * self.new_sale.quantity)
        self.assertEqual(last_personal_accounts.amount, self.last_personal_accounts_amount+last_tansactions.amount)
        self.assertEqual(self.new_sale.transaction, last_tansactions)
        self.assertEqual(transaction_wallet, last_tansactions.destination)

    def test_after_transaction_creation_amount_is_applied(self):
        self.assertEqual(self.new_wallet.amount, 0)
        wallet_ammount = self.new_wallet.amount
        new_transaction = Transactions.objects.create(destination=self.new_wallet, description="Venta locrito", date=self.now, amount=1000)
        self.assertEqual(self.new_wallet.amount, new_transaction.amount + wallet_ammount)

    def test_merge_two_accounts(self):
        new_account = AccountStatus.objects.create(name='nombre_de_la_cuenta_padre_test_merge',start=date.today())
        second_account = AccountStatus.objects.create(name='nombre_de_la_cuenta_test_merge',start=date.today())
        first_transaction = Transactions.objects.create(destination=new_account.wallet, description="Primera transaccion", date=date.today(), amount=1000)
        second_transaction = Transactions.objects.create(destination=new_account.wallet, description="Segunda transaccion", date=date.today(), amount=-500)
        self.assertFalse(new_account.merge_account(second_account))
        account_closed = new_account.close_account()
        ammount_moved = new_account.get_account_balance()
        self.assertTrue(account_closed)
        merge_accounts = new_account.merge_account(second_account)
        last_transaction = Transactions.objects.last()
        ignored_transaction = Transactions.objects.get(name = "Uniendo Cuentas " + str(new_account.id))
        self.assertIsNotNone(ignored_transaction)
        self.assertTrue(merge_accounts)
        self.assertEqual(second_account.wallet.amount, ammount_moved)
        self.assertEqual(new_account.get_account_balance(), ammount_moved)
