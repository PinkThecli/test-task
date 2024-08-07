# Тестовое задание для вакансии
## Вопрос №1
Ответ в task1.py. Была предложена реализация через операцию побитового и. Данная реализация занимает меньше процессорных инструкций, чем вариант через остаток от деления, то есть предложенная функция будет выполняться быстрее. Однако изначальная реализация обладает лучшими читаемостью и прозрачностью, чем предложенная.  
## Вопрос №2
Ответ в task2.py. Было предложено две реализации циклического буфера FIFO. Класс CycleBuffer1 реализован с использованием указателей (индексов) на начало и конец данных, класс CycleBuffer2 -- с использованием указателя (индекса) на начало данных и их длины. Сравнение по быстродействию показало, что вторая реализация почти в 2 раза быстрее, чем первая. Это связано с тем, что расчет длины данных во втором варианте происходит через обращение к соответствующему параметру, что значительно быстрее, чем постоянный перерасчет в первом варианте. Кроме того, из-за использования деления без остатка в методах add/pop в них так же отсутствуют медленные конструкции if/else, что тоже вносит свой вклад в быстродействие.  
## Вопрос №3
Ответ в task3.py. Был реализован алгоритм сортировки слиянием. Данный алгоритм разделяет массив на части и сортирует их по отдельности. Данный подход значительно уменьшает число сравнений в ходе сортировки, что сильно экономит такты процессора. Данный алгоритм обладает постоянной сложностью O(nlogn) даже для худших случаев, что гарантирует его быстродействие в них. Однако, из-за этого же данный алгоритм не очень эффективен при использовании на частично или полностью отсортированных массивах. Из-за своей же сложности он также оказывается эффективным при больших размерах массива. Кроме того, алгоритм сортировки слиянием благодаря своей структуре может быть распараллелен на нескольких процессорных ядрах, что еще в разы уменьшит число затрачиваемых тактов. Учитывая все вышесказанное, можно утверждать, что данный алгоритм является наиболее быстрым по процессорным тактам для сортировки заданного массива чисел.