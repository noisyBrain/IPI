from tp2.dir_ex_5.refactor_ex_5 import qualifies_for_discount


def test_customer_qualified_for_discount():
    week_day = 'LUNES'
    amount_articles = 4

    qualifies = qualifies_for_discount(week_day, amount_articles)

    assert qualifies == 'Accede al descuento'


def test_customer_not_qualified_for_discount_because_is_not_day_off():
    week_day = 'MIERCOLES'
    amount_articles = 4

    qualifies = qualifies_for_discount(week_day, amount_articles)

    assert qualifies == None


def test_customer_not_qualified_for_discount_because_did_not_buy_enough_articles():
    week_day = 'LUNES'
    amount_articles = 2

    qualifies = qualifies_for_discount(week_day, amount_articles)

    assert qualifies == None
