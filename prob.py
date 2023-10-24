import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class LoggingMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger(self.__class__.__name__)

    def log(self, message, level=logging.INFO):
        self.logger.log(level, message)


class Discount:
    def discount(self):
        raise NotImplementedError


class RegularDiscount(Discount):
    def discount(self):
        return 0.9


class SilverDiscount(Discount):
    def discount(self):
        return 0.85


class GoldDiscount(Discount):
    def discount(self):
        return 0.8


class Product:
    def __init__(self, title: str):
        self.title = title

    def __str__(self):
        return f'{self.title}:'


class Cart(LoggingMixin):
    def __init__(self, discount: Discount = None):
        super(Cart, self).__init__()
        self.__products = []
        self.__quantities = []
        self.__price = []
        self.discount = discount

    def add_product(self, product: Product, quantity: int | float = 1, many=0):
        if isinstance(product, Product) and isinstance(quantity, int | float) and many > 0:
            self.log('Add product to Cart')
            self.__products.append(product)
            self.__quantities.append(quantity)
            self.__price.append(many)
        else:
            self.log(f'wrong price {product}', logging.WARNING)

    def total(self):
        summa = sum(many * quantity for product, quantity, many in zip(self.__products, self.__quantities, self.__price))
        summa = summa * self.discount.discount() if self.discount else summa
        self.log(f'Customer pay {summa}', logging.INFO)
        return summa

    def __str__(self):
        return '\n'.join(map(lambda items: f'{items[0]}{items[2]} x {items[1]} = {items[1] * items[2]} UAH',
                          zip(self.__products, self.__quantities, self.__price))) + f'\nTotal: {self.total():.2f} UAH\n'


pr_1 = Product('banana')
pr_2 = Product('apple')
pr_3 = Product('orange')


cart_1 = Cart()
cart_2 = Cart(SilverDiscount())

cart_1.add_product(pr_1,2,6)
cart_1.add_product(pr_2,3,3)
cart_1.add_product(pr_2,2,6)
cart_1.add_product(pr_3,3,8)

cart_2.add_product(pr_1,5,5)

print(cart_1)
print(cart_2)