from pandas import DataFrame
from matplotlib import pyplot


def two_pow_x():
    two_pow_x_dataframe = DataFrame({'x': range(-10, 11)})
    two_pow_x_dataframe['y'] = 2.0 ** two_pow_x_dataframe['x']
    print(two_pow_x_dataframe)

    pyplot.plot(two_pow_x_dataframe.x, two_pow_x_dataframe.y, color="red")
    pyplot.xlabel('x')
    pyplot.ylabel('y')
    pyplot.grid()
    pyplot.axhline()
    pyplot.axvline()
    pyplot.show()


def deposit_calculator():
    base = 1000
    interest_rate = 1.05
    deposit_dataframe = DataFrame({'x': range(0, 21)})
    deposit_dataframe['y'] = base * interest_rate ** deposit_dataframe['x']
    print(deposit_dataframe)

    pyplot.plot(deposit_dataframe.x, deposit_dataframe.y, color="red")
    pyplot.xlabel('year')
    pyplot.ylabel('total')
    pyplot.grid()
    pyplot.axhline()
    pyplot.axvline()
    pyplot.show()


if __name__ == "__main__":
    two_pow_x()
    deposit_calculator()
