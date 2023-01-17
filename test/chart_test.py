from utils.chart import Chart

def test0():
    chart = Chart(10)
    chart['key'] = [i for i in range(10)]
    print(chart['key'])
    print(chart[4])
    print(chart['key',4])
    
    print(chart['key',1])
    chart['key',1] = 2
    print(chart['key',1])
    chart[2] = {'key':99}
    print(chart[2])
    chart['key',2] = 98
    print(chart['key',2])
    chart.add_row('key1')
    chart[2] = {'key1':199}
    print(chart[2])
    print(chart[3])
    return

if __name__ == '__main__':
    test0()