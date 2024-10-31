from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.metrics import sp
import random
import math


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        super(HomeScreen, self).__init__(**kwargs)

        self.label = Label(text='Choose a mathematical cryptographic operation:',
                           size_hint=(.5, .1), pos_hint={'center_x': .5, 'center_y': .9})

        self.exp_button = Button(text='Modular Exponentiation', size_hint=(.6, .06), pos_hint={
                                 'center_x': .5, 'center_y': .79}, on_press=self.show_exp_screen)
        self.gcd_button = Button(text='Greatest Common Divisor', size_hint=(.6, .06), pos_hint={
                                 'center_x': .5, 'center_y': .73}, on_press=self.show_gcd_screen)
        self.mi_button = Button(text='Multiplicative Inverse', size_hint=(.6, .06), pos_hint={
                                'center_x': .5, 'center_y': .67}, on_press=self.show_mi_screen)
        self.mrp_button = Button(text='Miller-Rabin Primality', size_hint=(.6, .06), pos_hint={
                                 'center_x': .5, 'center_y': .61}, on_press=self.show_mrp_screen)
        self.fp_button = Button(text='Fermat Prime Factrization', size_hint=(.6, .06), pos_hint={
            'center_x': .5, 'center_y': .55}, on_press=self.show_fp_screen)
        self.etf_button = Button(text='Euler Totient Function', size_hint=(.6, .06), pos_hint={
                                 'center_x': .5, 'center_y': .49}, on_press=self.show_etf_screen)
        self.eth_button = Button(text='Euler Theorem', size_hint=(.6, .06), pos_hint={
            'center_x': .5, 'center_y': .43}, on_press=self.show_eth_screen)
        self.crt_button = Button(text='Chinese Remainder Therorem', size_hint=(.6, .06), pos_hint={
                                 'center_x': .5, 'center_y': .37}, on_press=self.show_crt_screen)
        self.cp_button = Button(text='Coprimality Test', size_hint=(.6, .06), pos_hint={
            'center_x': .5, 'center_y': .31}, on_press=self.show_cp_screen)
        self.dl_button = Button(text='Discrete Log Problem', size_hint=(.6, .06), pos_hint={
            'center_x': .5, 'center_y': .25}, on_press=self.show_dl_screen)

        self.add_widget(self.label)
        self.add_widget(self.exp_button)
        self.add_widget(self.gcd_button)
        self.add_widget(self.mi_button)
        self.add_widget(self.mrp_button)
        self.add_widget(self.fp_button)
        self.add_widget(self.etf_button)
        self.add_widget(self.eth_button)
        self.add_widget(self.crt_button)
        self.add_widget(self.cp_button)
        self.add_widget(self.dl_button)

        self.add_widget(Label(text='Made with <3 by Vrungee',
                        size_hint_y=None, height=sp(24)))

    def show_exp_screen(self, instance):
        self.manager.get_screen('exp_screen').update_input_fields()
        self.manager.current = 'exp_screen'

    def show_gcd_screen(self, instance):
        self.manager.get_screen('gcd_screen').update_input_fields()
        self.manager.current = 'gcd_screen'

    def show_mi_screen(self, instance):
        self.manager.get_screen('mi_screen').update_input_fields()
        self.manager.current = 'mi_screen'

    def show_mrp_screen(self, instance):
        self.manager.get_screen('mrp_screen').update_input_fields()
        self.manager.current = 'mrp_screen'

    def show_fp_screen(self, instance):
        self.manager.get_screen('fp_screen').update_input_fields()
        self.manager.current = 'fp_screen'

    def show_etf_screen(self, instance):
        self.manager.get_screen('etf_screen').update_input_fields()
        self.manager.current = 'etf_screen'

    def show_eth_screen(self, instance):
        self.manager.get_screen('eth_screen').update_input_fields()
        self.manager.current = 'eth_screen'

    def show_crt_screen(self, instance):
        self.manager.get_screen('crt_screen').update_input_fields()
        self.manager.current = 'crt_screen'

    def show_cp_screen(self, instance):
        self.manager.get_screen('cp_screen').update_input_fields()
        self.manager.current = 'cp_screen'

    def show_dl_screen(self, instance):
        self.manager.get_screen('dl_screen').update_input_fields()
        self.manager.current = 'dl_screen'


class ExpScreen(Screen):
    def __init__(self, **kwargs):
        super(ExpScreen, self).__init__(**kwargs)

        self.label = Label(text='Modular Exponentiation (a^b mod m)',
                           size_hint=(.5, .1), pos_hint={'center_x': .5, 'center_y': .9})

        self.label_a = Label(text='a:', size_hint=(None, None), size=(
            sp(30), sp(30)), pos_hint={'center_x': 0.2, 'center_y': 0.75})
        self.a = TextInput(size_hint=(None, None), size=(sp(100), sp(
            40)), multiline=False, pos_hint={'center_x': .5, 'center_y': .75}, input_type='number')

        self.label_b = Label(text='b:', size_hint=(None, None), size=(
            sp(30), sp(30)), pos_hint={'center_x': 0.2, 'center_y': 0.65})
        self.b = TextInput(size_hint=(None, None), size=(sp(100), sp(
            40)), multiline=False, pos_hint={'center_x': .5, 'center_y': .65}, input_type='number')

        self.label_m = Label(text='m:', size_hint=(None, None), size=(
            sp(30), sp(30)), pos_hint={'center_x': 0.2, 'center_y': 0.55})
        self.m = TextInput(size_hint=(None, None), size=(sp(100), sp(
            40)), multiline=False, pos_hint={'center_x': .5, 'center_y': .55}, input_type='number')

        self.result_label = Label(text='', size_hint=(.3, .1), pos_hint={
                                  'center_x': .5, 'center_y': .4})
        self.back_button = Button(text='Back', size_hint=(.1, .1), pos_hint={
                                  'center_x': .9, 'center_y': .1}, on_press=self.back_to_home)
        self.calculate_button = Button(text='Calculate', size_hint=(.3, .1), pos_hint={
                                       'center_x': .5, 'center_y': .3}, on_press=self.calculate_exp)

        self.add_widget(self.label)
        self.add_widget(self.label_a)
        self.add_widget(self.a)
        self.add_widget(self.label_b)
        self.add_widget(self.b)
        self.add_widget(self.label_m)
        self.add_widget(self.m)
        self.add_widget(self.result_label)
        self.add_widget(self.back_button)
        self.add_widget(self.calculate_button)

    def update_input_fields(self):
        self.a.text = ''
        self.b.text = ''
        self.m.text = ''
        self.result_label.text = ''

    def back_to_home(self, instance):
        self.manager.current = 'home'

    def calculate_exp(self, instance):
        try:
            a = int(self.a.text)
            b = int(self.b.text)
            m = int(self.m.text)
            result = pow(a, b, m)
            self.result_label.text = f'Result: {result}'
        except Exception as e:
            self.result_label.text = f'Error: {e}'


class GcdScreen(Screen):
    def __init__(self, **kwargs):
        super(GcdScreen, self).__init__(**kwargs)

        self.label = Label(text='Greatest Common Divisor (GCD(n1, n2))',
                           size_hint=(.5, .1), pos_hint={'center_x': .5, 'center_y': .9})

        self.label_n1 = Label(text="n1:", size_hint=(None, None), pos_hint={
                              'center_x': 0.2, 'center_y': 0.75})
        self.n1 = TextInput(size_hint=(None, None), size=(
            sp(100), sp(40)), multiline=False, pos_hint={'center_x': 0.5, 'center_y': 0.75}, input_type='number')

        self.label_n2 = Label(text="n2:", size_hint=(None, None), pos_hint={
                              'center_x': 0.2, 'center_y': 0.65})
        self.n2 = TextInput(size_hint=(None, None), size=(
            sp(100), sp(40)), multiline=False, pos_hint={'center_x': 0.5, 'center_y': 0.65}, input_type='number')

        self.result_label = Label(text='', size_hint=(None, None), pos_hint={
                                  'center_x': 0.5, 'center_y': 0.5})

        self.back_button = Button(text='Back', size_hint=(None, None), size=(
            sp(100), sp(50)), pos_hint={'center_x': 0.2, 'center_y': 0.35}, on_press=self.back_to_home)
        self.calculate_button = Button(text='Calculate', size_hint=(None, None), size=(
            sp(150), sp(50)), pos_hint={'center_x': 0.7, 'center_y': 0.35}, on_press=self.calculate_gcd)

        self.add_widget(self.label)
        self.add_widget(self.label_n1)
        self.add_widget(self.n1)
        self.add_widget(self.label_n2)
        self.add_widget(self.n2)
        self.add_widget(self.result_label)
        self.add_widget(self.back_button)
        self.add_widget(self.calculate_button)

    def calculate_gcd(self, instance):
        try:
            n1 = int(self.n1.text)
            n2 = int(self.n2.text)
            result = gcd(n1, n2)
            self.result_label.text = f'Result: {result}'
        except Exception as e:
            self.result_label.text = f'Error: {e}'

    def update_input_fields(self):
        self.n1.text = ''
        self.n2.text = ''
        self.result_label.text = ''

    def back_to_home(self, instance):
        self.manager.current = 'home'

    def calculate_gcd(self, instance):
        try:
            n1 = int(self.n1.text)
            n2 = int(self.n2.text)
            result = gcd(n1, n2)
            self.result_label.text = f'Result: {result}'
        except Exception as e:
            self.result_label.text = f'Error: {e}'


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


class MIScreen(Screen):
    def __init__(self, **kwargs):
        super(MIScreen, self).__init__(**kwargs)

        self.label = Label(text='Multiplicative Inverse (a*MI congruent 1 mod n)',
                           size_hint=(.5, .1), pos_hint={'center_x': .5, 'center_y': .9})

        self.label_a = Label(text="a:", size_hint=(None, None), pos_hint={
                             'center_x': 0.2, 'center_y': 0.75})
        self.a = TextInput(size_hint=(None, None), size=(
            sp(100), sp(40)), multiline=False, pos_hint={'center_x': 0.5, 'center_y': 0.75}, input_type='number')

        self.label_n = Label(text="n:", size_hint=(None, None), pos_hint={
                             'center_x': 0.2, 'center_y': 0.65})
        self.n = TextInput(size_hint=(None, None), size=(
            sp(100), sp(40)), multiline=False, pos_hint={'center_x': 0.5, 'center_y': 0.65}, input_type='number')

        self.result_label = Label(text='', size_hint=(None, None), pos_hint={
                                  'center_x': 0.5, 'center_y': 0.5})

        self.back_button = Button(text='Back', size_hint=(None, None), size=(
            sp(100), sp(50)), pos_hint={'center_x': 0.2, 'center_y': 0.35}, on_press=self.back_to_home)
        self.calculate_button = Button(text='Calculate', size_hint=(None, None), size=(
            sp(150), sp(50)), pos_hint={'center_x': 0.7, 'center_y': 0.35}, on_press=self.calculate_mi)

        self.add_widget(self.label)
        self.add_widget(self.label_a)
        self.add_widget(self.a)
        self.add_widget(self.label_n)
        self.add_widget(self.n)
        self.add_widget(self.result_label)
        self.add_widget(self.back_button)
        self.add_widget(self.calculate_button)

    def update_input_fields(self):
        self.a.text = ''
        self.n.text = ''
        self.result_label.text = ''

    def back_to_home(self, instance):
        self.manager.current = 'home'

    def calculate_mi(self, instance):
        try:
            a = int(self.a.text)
            n = int(self.n.text)
            gcd, x, y = eea(a, n)
            if gcd != 1:
                result = "Inverse doesn't exist"
            else:
                result = (x % n + n) % n  # Ensure result is positive
            self.result_label.text = f"Result: {result}"
        except Exception as e:
            self.result_label.text = f"Error: {e}"


def eea(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = eea(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


class MRPScreen(Screen):
    def __init__(self, **kwargs):
        super(MRPScreen, self).__init__(**kwargs)
        self.label = Label(text='Miller-Rabin Primality Test',
                           size_hint=(.5, .1), pos_hint={'center_x': .5, 'center_y': .9})
        self.label_n = Label(text="n:", size_hint=(None, None), pos_hint={
                             'center_x': 0.2, 'center_y': 0.75})
        self.n = TextInput(size_hint=(None, None), size=(
            sp(100), sp(40)), multiline=False, pos_hint={'center_x': 0.5, 'center_y': 0.75}, input_type='number')

        self.result_label = Label(text='', size_hint=(None, None), pos_hint={
                                  'center_x': 0.5, 'center_y': 0.5})
        self.back_button = Button(text='Back', size_hint=(None, None), size=(
            sp(100), sp(50)), pos_hint={'center_x': 0.2, 'center_y': 0.35}, on_press=self.back_to_home)
        self.calculate_button = Button(text='Calculate', size_hint=(None, None), size=(
            sp(150), sp(50)), pos_hint={'center_x': 0.7, 'center_y': 0.35}, on_press=self.calculate_mrp)

        self.add_widget(self.label)
        self.add_widget(self.label_n)
        self.add_widget(self.n)
        self.add_widget(self.result_label)
        self.add_widget(self.back_button)
        self.add_widget(self.calculate_button)

    def update_input_fields(self):
        self.n.text = ''
        self.result_label.text = ''

    def back_to_home(self, instance):
        self.manager.current = 'home'

    def calculate_mrp(self, instance):
        try:
            n = int(self.n.text)
            result = mrp(n)
            self.result_label.text = f'Is it Prime?: {result}'
        except Exception as e:
            self.result_label.text = f'Error: {e}'


def mrp(n, k=10):  # number of tests to run
    if n in [2, 3]:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Step 1: write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Step 2 and 3:
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


class FPScreen(Screen):
    def __init__(self, **kwargs):
        super(FPScreen, self).__init__(**kwargs)
        self.label = Label(text='Fermat Prime Factorization',
                           size_hint=(.5, .1), pos_hint={'center_x': .5, 'center_y': .9})
        self.label_n = Label(text="n:", size_hint=(None, None), pos_hint={
                             'center_x': 0.2, 'center_y': 0.75})
        self.n = TextInput(size_hint=(None, None), size=(
            sp(100), sp(40)), multiline=False, pos_hint={'center_x': 0.5, 'center_y': 0.75}, input_type='number')

        self.result_label = Label(text='', size_hint=(None, None), pos_hint={
                                  'center_x': 0.5, 'center_y': 0.5})
        self.back_button = Button(text='Back', size_hint=(None, None), size=(
            sp(100), sp(50)), pos_hint={'center_x': 0.2, 'center_y': 0.35}, on_press=self.back_to_home)
        self.calculate_button = Button(text='Calculate', size_hint=(None, None), size=(
            sp(150), sp(50)), pos_hint={'center_x': 0.7, 'center_y': 0.35}, on_press=self.calculate_fp)

        self.add_widget(self.label)
        self.add_widget(self.label_n)
        self.add_widget(self.n)
        self.add_widget(self.result_label)
        self.add_widget(self.back_button)
        self.add_widget(self.calculate_button)

    def update_input_fields(self):
        self.n.text = ''
        self.result_label.text = ''

    def back_to_home(self, instance):
        self.manager.current = 'home'

    def calculate_fp(self, instance):
        try:
            n = int(self.n.text)
            result = fp(n)
            self.result_label.text = f'Prime Factors: {result}'
        except Exception as e:
            self.result_label.text = f'Error: {e}'


def fp(n):
    assert n % 2 != 0 and n >= 0, "n must be an odd non-negative integer"

    # Check if n is a perfect square
    if math.isqrt(n) ** 2 == n:
        raise ValueError("n must not be a perfect square")

    a = math.isqrt(n)
    b2 = a ** 2 - n
    while not math.isqrt(abs(b2)) ** 2 == abs(b2):
        a += 1
        b2 = a ** 2 - n
    p = a + math.isqrt(abs(b2))
    q = a - math.isqrt(abs(b2))
    return p, q


class ETFScreen(Screen):
    def __init__(self, **kwargs):
        super(ETFScreen, self).__init__(**kwargs)
        self.label = Label(text='Euler Totient Function = phi(n)',
                           size_hint=(.5, .1), pos_hint={'center_x': .5, 'center_y': .9})
        self.label_n = Label(text="n:", size_hint=(None, None), pos_hint={
                             'center_x': 0.2, 'center_y': 0.75})
        self.n = TextInput(size_hint=(None, None), size=(
            sp(100), sp(40)), multiline=False, pos_hint={'center_x': 0.5, 'center_y': 0.75}, input_type='number')

        self.result_label = Label(text='', size_hint=(None, None), pos_hint={
                                  'center_x': 0.5, 'center_y': 0.5})
        self.back_button = Button(text='Back', size_hint=(None, None), size=(
            sp(100), sp(50)), pos_hint={'center_x': 0.2, 'center_y': 0.35}, on_press=self.back_to_home)
        self.calculate_button = Button(text='Calculate', size_hint=(None, None), size=(
            sp(150), sp(50)), pos_hint={'center_x': 0.7, 'center_y': 0.35}, on_press=self.calculate_etf)

        self.add_widget(self.label)
        self.add_widget(self.label_n)
        self.add_widget(self.n)
        self.add_widget(self.result_label)
        self.add_widget(self.back_button)
        self.add_widget(self.calculate_button)

    def update_input_fields(self):
        self.n.text = ''
        self.result_label.text = ''

    def back_to_home(self, instance):
        self.manager.current = 'home'

    def calculate_etf(self, instance):
        try:
            n = int(self.n.text)
            result = etf(n)
            self.result_label.text = f'Result: {result}'
        except Exception as e:
            self.result_label.text = f'Error: {e}'


def etf(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result


class ETHScreen(Screen):
    def __init__(self, **kwargs):
        super(ETHScreen, self).__init__(**kwargs)

        self.label = Label(text='Euler Theorem (a^phi(n) congruent 1 mod n)',
                           size_hint=(.5, .1), pos_hint={'center_x': .5, 'center_y': .9})

        self.label_a = Label(text="a:", size_hint=(None, None), pos_hint={
                             'center_x': 0.2, 'center_y': 0.75})
        self.a = TextInput(size_hint=(None, None), size=(
            sp(100), sp(40)), multiline=False, pos_hint={'center_x': 0.5, 'center_y': 0.75}, input_type='number')

        self.label_n = Label(text="n:", size_hint=(None, None), pos_hint={
                             'center_x': 0.2, 'center_y': 0.65})
        self.n = TextInput(size_hint=(None, None), size=(
            sp(100), sp(40)), multiline=False, pos_hint={'center_x': 0.5, 'center_y': 0.65}, input_type='number')

        self.result_label = Label(text='', size_hint=(None, None), pos_hint={
                                  'center_x': 0.5, 'center_y': 0.5})

        self.back_button = Button(text='Back', size_hint=(None, None), size=(
            sp(100), sp(50)), pos_hint={'center_x': 0.2, 'center_y': 0.35}, on_press=self.back_to_home)
        self.calculate_button = Button(text='Calculate', size_hint=(None, None), size=(
            sp(150), sp(50)), pos_hint={'center_x': 0.7, 'center_y': 0.35}, on_press=self.calculate_eth)

        self.add_widget(self.label)
        self.add_widget(self.label_a)
        self.add_widget(self.a)
        self.add_widget(self.label_n)
        self.add_widget(self.n)
        self.add_widget(self.result_label)
        self.add_widget(self.back_button)
        self.add_widget(self.calculate_button)

    def update_input_fields(self):
        self.a.text = ''
        self.n.text = ''
        self.result_label.text = ''

    def back_to_home(self, instance):
        self.manager.current = 'home'

    def calculate_eth(self, instance):
        try:
            a = int(self.a.text)
            n = int(self.n.text)
            result = eth(a, n)
            self.result_label.text = f'Euler Theorem true?: {result}'
        except Exception as e:
            self.result_label.text = f"Error: {e}"


def eth(a, n):
    phi_n = etf(n)
    result = pow(a, phi_n, n)
    return result == True


class CRScreen(Screen):
    def __init__(self, **kwargs):
        super(CRScreen, self).__init__(**kwargs)

        self.label = Label(text='Chinese Remainder Theorem\n(X[i] congruent a[i] mod m[i])', size_hint=(.5, .1), pos_hint={
                           'center_x': .5, 'center_y': .9})

        self.moduli_label = Label(text="Moduli (m)\n(int comma seperated):", size_hint=(
            None, None), pos_hint={'center_x': 0.25, 'center_y': 0.75})
        self.moduli = TextInput(size_hint=(None, None), size=(
            sp(80), sp(40)), multiline=False, pos_hint={'center_x': 0.75, 'center_y': 0.75}, input_type='number')

        self.remainders_label = Label(text="Remainders (a)\n(int comma separated):", size_hint=(
            None, None), pos_hint={'center_x': 0.25, 'center_y': 0.65})
        self.remainders = TextInput(size_hint=(None, None), size=(
            sp(80), sp(40)), multiline=False, pos_hint={'center_x': 0.75, 'center_y': 0.65}, input_type='number')

        self.result_label = Label(text='', size_hint=(None, None), pos_hint={
                                  'center_x': 0.5, 'center_y': 0.5})

        self.back_button = Button(text='Back', size_hint=(None, None), size=(
            sp(100), sp(50)), pos_hint={'center_x': 0.2, 'center_y': 0.35}, on_press=self.back_to_home)
        self.calculate_button = Button(text='Calculate', size_hint=(None, None), size=(
            sp(150), sp(50)), pos_hint={'center_x': 0.7, 'center_y': 0.35}, on_press=self.calculate_crt)

        self.add_widget(self.label)
        self.add_widget(self.moduli_label)
        self.add_widget(self.moduli)
        self.add_widget(self.remainders_label)
        self.add_widget(self.remainders)
        self.add_widget(self.result_label)
        self.add_widget(self.back_button)
        self.add_widget(self.calculate_button)

    def update_input_fields(self):
        self.moduli.text = ''
        self.remainders.text = ''
        self.result_label.text = ''

    def back_to_home(self, instance):
        self.manager.current = 'home'

    def calculate_crt(self, instance):
        try:
            moduli = list(map(int, self.moduli.text.split(',')))
            remainders = list(map(int, self.remainders.text.split(',')))
            result = chinese_remainder_theorem(moduli, remainders)
            self.result_label.text = f'Chinese Remainder Theorem result: {result}'
        except Exception as e:
            self.result_label.text = f"Error: {e}"


def chinese_remainder_theorem(moduli, remainders):
    # Calculate the product of all moduli
    prod = math.prod(moduli)

    result = 0
    for mi, ai in zip(moduli, remainders):
        # Compute the product of all moduli except mi
        prod_except_mi = prod // mi
        # Use modular inverse to find the coefficient
        coef = pow(prod_except_mi, -1, mi)
        # Add the term to the result
        result += ai * prod_except_mi * coef

    # Reduce the result modulo the product of all moduli
    return result % prod


class CPScreen(Screen):
    def __init__(self, **kwargs):
        super(CPScreen, self).__init__(**kwargs)

        self.label = Label(text='Coprimality Test',
                           size_hint=(.5, .1), pos_hint={'center_x': .5, 'center_y': .9})

        self.label_n1 = Label(text="n1:", size_hint=(None, None), pos_hint={
            'center_x': 0.2, 'center_y': 0.75})
        self.n1 = TextInput(size_hint=(None, None), size=(
            sp(100), sp(40)), multiline=False, pos_hint={'center_x': 0.5, 'center_y': 0.75}, input_type='number')

        self.label_n2 = Label(text="n2:", size_hint=(None, None), pos_hint={
            'center_x': 0.2, 'center_y': 0.65})
        self.n2 = TextInput(size_hint=(None, None), size=(
            sp(100), sp(40)), multiline=False, pos_hint={'center_x': 0.5, 'center_y': 0.65}, input_type='number')

        self.result_label = Label(text='', size_hint=(None, None), pos_hint={
                                  'center_x': 0.5, 'center_y': 0.5})

        self.back_button = Button(text='Back', size_hint=(None, None), size=(
            sp(100), sp(50)), pos_hint={'center_x': 0.2, 'center_y': 0.35}, on_press=self.back_to_home)
        self.calculate_button = Button(text='Calculate', size_hint=(None, None), size=(
            sp(150), sp(50)), pos_hint={'center_x': 0.7, 'center_y': 0.35}, on_press=self.calculate_cp)

        self.add_widget(self.label)
        self.add_widget(self.label_n1)
        self.add_widget(self.n1)
        self.add_widget(self.label_n2)
        self.add_widget(self.n2)
        self.add_widget(self.result_label)
        self.add_widget(self.back_button)
        self.add_widget(self.calculate_button)

    def update_input_fields(self):
        self.n1.text = ''
        self.n2.text = ''
        self.result_label.text = ''

    def back_to_home(self, instance):
        self.manager.current = 'home'

    def calculate_cp(self, instance):
        try:
            n1 = int(self.n1.text)
            n2 = int(self.n2.text)
            result = cp(n1, n2)
            self.result_label.text = f'Co-prime?: {result}'
        except Exception as e:
            self.result_label.text = f"Error: {e}"


def cp(a, b):
    return gcd(a, b) == 1


class DLScreen(Screen):
    def __init__(self, **kwargs):
        super(DLScreen, self).__init__(**kwargs)

        self.label = Label(text='Discrete Logarithm Problem (Log_b (a) mod m)', size_hint=(.5, .1), pos_hint={
                           'center_x': .5, 'center_y': .9})

        self.label_b = Label(text="b:", size_hint=(None, None), pos_hint={
                             'center_x': 0.2, 'center_y': 0.75})
        self.b = TextInput(size_hint=(None, None), size=(
            sp(100), sp(40)), multiline=False, pos_hint={'center_x': 0.5, 'center_y': 0.75}, input_type='number')

        self.label_a = Label(text="a:", size_hint=(None, None), pos_hint={
                             'center_x': 0.2, 'center_y': 0.65})
        self.a = TextInput(size_hint=(None, None), size=(
            sp(100), sp(40)), multiline=False, pos_hint={'center_x': 0.5, 'center_y': 0.65}, input_type='number')

        self.label_m = Label(text="m:", size_hint=(None, None), pos_hint={
                             'center_x': 0.2, 'center_y': 0.55})
        self.m = TextInput(size_hint=(None, None), size=(
            sp(100), sp(40)), multiline=False, pos_hint={'center_x': 0.5, 'center_y': 0.55}, input_type='number')

        self.result_label = Label(text='', size_hint=(None, None), pos_hint={
                                  'center_x': 0.5, 'center_y': 0.45})

        self.back_button = Button(text='Back', size_hint=(None, None), size=(
            sp(100), sp(50)), pos_hint={'center_x': 0.2, 'center_y': 0.35}, on_press=self.back_to_home)
        self.calculate_button = Button(text='Calculate', size_hint=(None, None), size=(
            sp(150), sp(50)), pos_hint={'center_x': 0.7, 'center_y': 0.35}, on_press=self.calculate_discrete_log)

        self.add_widget(self.label)
        self.add_widget(self.label_b)
        self.add_widget(self.b)
        self.add_widget(self.label_a)
        self.add_widget(self.a)
        self.add_widget(self.label_m)
        self.add_widget(self.m)
        self.add_widget(self.result_label)
        self.add_widget(self.back_button)
        self.add_widget(self.calculate_button)

    def update_input_fields(self):
        self.b.text = ''
        self.a.text = ''
        self.m.text = ''
        self.result_label.text = ''

    def back_to_home(self, instance):
        self.manager.current = 'home'

    def calculate_discrete_log(self, instance):
        try:
            b = int(self.b.text)
            a = int(self.a.text)
            m = int(self.m.text)
            result = dl(b, a, m)
            self.result_label.text = f'Result: {result}'
        except Exception as e:
            self.result_label.text = f"Error: {e}"


def dl(b, a, m):
    """
    Calculates the discrete logarithm of b with base a modulo m.
    :param b: The base number
    :param a: The number to find the logarithm of
    :param m: The modulus
    :return: The discrete logarithm or None if it does not exist
    """
    if not is_prime(m):
        raise ValueError("Modulus must be a prime number")

    for i in range(1, m):
        if pow(b, i, m) == a:
            return i

    return None


def is_prime(n):
    """
    Checks if a number is prime.
    :param n: The number to check
    :return: True if the number is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ExpScreen(name='exp_screen'))
        sm.add_widget(GcdScreen(name='gcd_screen'))
        sm.add_widget(MIScreen(name='mi_screen'))
        sm.add_widget(MRPScreen(name='mrp_screen'))
        sm.add_widget(FPScreen(name='fp_screen'))
        sm.add_widget(ETFScreen(name='etf_screen'))
        sm.add_widget(ETHScreen(name='eth_screen'))
        sm.add_widget(CRScreen(name='crt_screen'))
        sm.add_widget(CPScreen(name='cp_screen'))
        sm.add_widget(DLScreen(name='dl_screen'))
        return sm


if __name__ == '__main__':
    TestApp().run()
