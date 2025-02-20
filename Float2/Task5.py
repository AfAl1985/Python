print("Задача 5. Маятник")

# Что нужно сделать
# Известно, что амплитуда качающегося маятника с каждым разом затухает на 8,4% от амплитуды
# предыдущего колебания. Если качнуть маятник, то, строго говоря, он не остановится никогда,
# просто амплитуда будет постоянно уменьшаться до тех пор, пока мы не сочтём такой маятник
# остановившимся. Напишите программу, определяющую, сколько раз качнётся маятник, прежде чем он,
# по нашему мнению, остановится.
# Программа получает на вход начальную амплитуду колебания в сантиметрах
# и конечную амплитуду колебаний, которая считается остановкой маятника.
# Обеспечьте контроль ввода.
# Пример:
# Введите начальную амплитуду: 1
# Введите амплитуду остановки: 0.1
# Маятник считается остановившимся через 27 колебаний
def Amplitude(start_amp, stop_amp):
    count = 0
    while start_amp >= stop_amp:
        start_amp -= start_amp / 100 * 8.4
        count += 1
    return  count

def Check(start_amp, stop_amp):
    if start_amp < stop_amp:
        print('Error')
        Start()
    else:
        pendulum_stop = Amplitude(start_amp, stop_amp)
        return pendulum_stop

def Start():
    start_amp = int(input("Enter initial amplitude: "))
    stop_amp = float(input("Enter stop point: "))
    answer = Check(start_amp, stop_amp)
    print(answer)

Start()