import numpy as np
count = 0                            # счетчик попыток
number = np.random.randint(1,101)    # загадали число
print ("Загадано число от 1 до 100")

        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    min_number = 1 #задаем нижнюю границу поиска
    max_number = 101 # задаем верхнюю границу поиска
    predict = np.random.randint(1,101) # первый раз пытаемся угадать число
    
    while number != predict:
        count+=1
        if number > predict: 
            min_number = predict+1 # Если предпологаемое число меньше загаданого то меняем нижнюю границу поиска
        elif number < predict: 
            max_number = predict # Если предпологаемое число больше загаданого то меняем верхнюю границу поиска
        predict = np.random.randint(min_number,max_number) # попытка угадать число с новыми границами
    return(count) # выход из цикла, если угадали

def game_core_v3(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    min_number = 1 #задаем нижнюю границу поиска
    max_number = 101 # задаем верхнюю границу поиска
    predict = np.random.randint(1,101) # первый раз пытаемся угадать число
    
    while number != predict:
        count+=1
        if number > predict: 
            min_number = predict # Если предпологаемое число меньше загаданого то меняем нижнюю границу поиска
        elif number < predict: 
            max_number = predict # Если предпологаемое число больше загаданого то меняем верхнюю границу поиска
        #predict = np.random.randint(min_number,max_number) # попытка угадать число с новыми границами
        predict = min_number + (max_number-min_number)//2
    return(count) # выход из цикла, если угадали

# Проверяем
score_game(game_core_v3)