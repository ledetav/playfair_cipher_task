# 🔐 Playfair Cipher (Шифр Плейфера)

Реализация шифра Плейфера на Python с поддержкой всех классических правил.

## 📚 Описание

Шифр Плейфера — это симметричный ручной шифр, использующий биграммы и матрицу 5×5.

### Ключевые особенности реализации:

- Используется **английский алфавит без буквы J** (J заменяется на I).
- **Буква Q сохраняется** в таблице.
- Повторяющиеся буквы в биграммах разделяются `X`.
- Если в сообщении нечётное количество символов — в конец добавляется `X`.
- Шифруются пары символов по 4 классическим правилам:
  1. Повторы → `X`
  2. Одна строка → сдвиг вправо
  3. Один столбец → сдвиг вниз
  4. Прямоугольник → диагональная замена

---

## 🚀 Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/ledetav/playfair_cipher_task.git
cd playfair_cipher_task
```
2. (Опционально) создайте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows
```
3. Установите зависимости (если есть):

```bash
pip install -r requirements.txt
```

4. Запустите пример:

```bash
python main.py
```
---

## ✅ Запуск тестов

```bash
python -m unittest discover tests
```

или точечно:

```bash
python tests_playfair.py
```

Если всё работает, увидите что-то вроде:
```bash
..........
----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK
```
