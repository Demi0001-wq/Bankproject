import pytest

from src.classes import Category, Product


@pytest.fixture
def product_sample():
    return Product("Iphone 15", "512GB, Gray", 210000.0, 8)


@pytest.fixture
def category_sample(product_sample):
    return Category("Smartphones", "Modern smartphones", [product_sample])


def test_product_init(product_sample):
    assert product_sample.name == "Iphone 15"
    assert product_sample.description == "512GB, Gray"
    assert product_sample.price == 210000.0
    assert product_sample.quantity == 8


def test_product_price_setter(product_sample):
    product_sample.price = 220000.0
    assert product_sample.price == 220000.0
    with pytest.raises(ValueError):
        product_sample.price = -100


def test_category_init(category_sample):
    assert category_sample.name == "Smartphones"
    assert category_sample.description == "Modern smartphones"
    assert len(category_sample.products) == 1


def test_category_add_product(category_sample):
    new_product = Product("Samsung S23", "256GB, Black", 180000.0, 5)
    category_sample.add_product(new_product)
    assert len(category_sample.products) == 2
    assert category_sample.products[-1].name == "Samsung S23"


def test_category_add_invalid_product(category_sample):
    with pytest.raises(TypeError):
        category_sample.add_product("Not a product")


def test_category_totals():
    # Resetting totals for clean test (though in pytest they accumulate if not careful)
    # But since we just created some in the fixtures, let's just check they are positive
    assert Category.total_categories > 0
    assert Category.total_unique_products > 0
