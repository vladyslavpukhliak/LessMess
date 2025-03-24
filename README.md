<div align="center">
<h1>Less Mess</h1>
<h4>Допомагає зробити ваш ПК упорядкованішим.</h4>

<a href="#як-зробити-внесок-у-проект">Як зробити внесок у проект</a> • 
<a href="#короткий-опис">Як працює утиліта</a> • 
<a href="#завантажити">Завантажити</a> • 
<a href="https://u24.gov.ua">Зробити внесок у відбудову України</a>
</div>
<!-- 
<p align="center">
    <a href="https://github.com/vladyslavpukhliak/LessMess/releases/download/v1.0.0/LessMessInstaller.exe">
        <img src="https://img.shields.io/github/downloads/vladyslavpukhliak/lessmess/total.svg">
    </a>
</p> -->

Це безкоштовне програмне забезпечення з відкритим вихідним кодом.  
Ви можете **підтримати** мою працю, **зробивши внесок у відбудову шкіл та лікарень, облаштування бомбосховищ, розмінування України** на <a href="https://u24.gov.ua">платформі UNITED24</a>.

## Короткий опис
Less Mess — це сортувальник файлів за їхнім розширенням у відповідні папки з можливістю редагування конфігураційного файлу.  
Утиліта не прив'язана до конкретної операційної системи і працює виключно з тими директоріями і файлами розширення яких вказані у конфігураційному файлі `parameters.json`.  
Його можна знайти в папці з виконуваним файлом (утилітою) і відредагувати у будь-якому текстовому редакторі.

<div align="center">
    <img src="https://github.com/vladyslavpukhliak/LessMess/blob/main/Icons/lessmess.gif" alt="Screenshot" width="600"/>
</div>

## Налаштування конфігураційного файлу
<div align="center">
    <img src="https://github.com/vladyslavpukhliak/LessMess/blob/main/Icons/edit_config.gif" alt="How to edit config" width="600"/>
</div>
<br>

У конфігураційний файл попередньо вже записані найпопулярніші розширення файлів котрі будуть відсортовані по відповідним папкам: 
`~/Documents`, `~/Music`, `~/Videos`, `~/Pictures`, `~/Downloads/Archives`, `~/Downloads/Presentations`.  
Ви можете ознайомитися з <a href="https://github.com/vladyslavpukhliak/LessMess/blob/main/parameters.json">повним списком</a>.

Файл має таку структуру:

```json
{
    "track": "шлях досліджуваної директорії",

    "extension":{
        "шлях папки куди слід перенести з досліджуваної папки документи таких розширень":["розширення1",
 "розширення2", "розширення3"],
        
        "шлях іншої директорії":["розширення4"]
    }
}
```

Приклад реального конфігураційного файла `parameters.json`:

```json
{
    "track": "~/Downloads",

    "extension":{
        "~/Downloads/Текстові документи":["txt","docx","doc","pdf"],
        
        "~/Music":["mp3", "wav", "flac"],

        "~/Music/Ноти":["gp","gpx","mid","mxl","mscz"],

        "~/Music/DAW":["flp", "logicx", "cpr", "als"],

        "~/Downloads/Творчість/Графіка":["psd","kra","ai","xcf","cdr"],

        "~/Videos":["mp4", "mkv", "mov", "avi", "webm"],
        
        "~/Pictures":["jpg", "png", "svg", "webp", "gif", "ico"],

        "D:/Development/3D Modeling":["obj","fbx","stl","max","blend","c4d"],

        "D:/Development/Scripts":["cs","py","js","java","ts","c","h","cpp","hpp","php"]
    }
}
```

1. Ви можете змінити шлях досліджуваної директорії `"track"` (за замовчуванням це `"~/Downloads"`).  
2. Шлях директорії вказується в подвійних лапках. Після — має йти `:` і квадратні дужки `[]`.  
3. Ви можете дописувати розширення (без крапок перед ними чи пробілів) в подвійних лапках через кому в середині квадратних дужок `[]`.  
4. Ви можете додати (скопіювати попередню і відредагувати) категорію через кому всередині фігурних дужок `"extension":{ }`. Це означатиме, що якщо цієї папки не існує, утиліта створить її самостійно перед тим, як почне переносити туди файли.  
5. Або можете прибрати категорію взагалі. Пам'ятайте, **в останньої категорії** після квадратних дужок `[]` **не має бути коми у кінці**.  
6. Не забувайте візуально звірити відредагований конфігураційний файл з прикладом або резервною копією.  

**Зверніть увагу на деякі особливості:**
+ Шлях `"~/"` відповідає `"C:/Users/ім'я користувача/"` у ОС Windows або `"/home/ім'я користувача/"` у UNIX-подібних ОС.  
Якщо утиліта має працювати з іншими папками або жорсткими дисками — вкажіть повний шлях до них.  
+ Шлях до системних директорій, наведених у прикладі конфігураційного файлу (`Відео`, `Зображення`, `Документи`), бажано вказувати англійською мовою або скопіювати повний шлях з файлового менеджера.
+ Якщо файл із такою назвою вже існуватиме в одній із папок, утиліта запропонує перейменувати його, додавши до назви закінчення `"_duplicate"`. Якщо натиснути кнопку `"Ні"`, утиліта просто проігнорує цей файл.
+ Утиліта закривається одразу після завершення сортування і не працює до наступного запуску.
+ Файл `parameters.json` має бути в одній директорії з виконуваним файлом (утилітою).
+ Рекомендація: робіть резервні копії конфігураційного файлу перед його зміною, можете назвати її наприклад `parameters_old.json`. Потім можете просто перейменувати її на `parameters.json` тим самим замінивши конфігураційний файл.

## Завантажити
<a href="https://github.com/vladyslavpukhliak/LessMess/releases/download/v1.0.0/LessMessInstaller.exe">Інсталятор для ОС Windows</a> дозволяє реалізувати запуск утиліти разом з системою або з контекстного меню.
<br><br>
Рекомендація: оберіть шлях, куди буде встановлена утиліта. Якщо буде обрано шлях за замовчуванням, на кшталт `"C:\Program Files (x86)\Less Mess"`, майте на увазі, що вам слід буде змінити права адміністратора для папки утиліти `"Less Mess"`, аби мати змогу змінювати файл конфігурації `parameters.json`.  
Змінити права адміністратора для папки `"Less Mess"` можна натиснувши правою кнопною миші на неї → `Властивості` → `Безпека` → `Змінити...`. Оберіть користувача або кількох → `Повний доступ` → `Застосувати`.

## Як зробити внесок у проект

1. Клонуйте репозиторій і створіть нову гілку:  
`$ git checkout https://github.com/vladyslavpukhliak/LessMess -b ім'я_для_нової_гілки`.  
2. Внесіть зміни та протестуйте  
3. Надішліть Pull Request з вичерпним описом змін

## Використані джерела

- [PyInstaller](https://pyinstaller.org/en/stable/) & [Auto-Py-To-Exe](https://pypi.org/project/auto-py-to-exe/) (GUI) — компілятор Python коду в єдиний виконуваний файл (.exe).
- [Inno Setup](https://jrsoftware.org/isinfo.php) — система створення інсталяторів для Windows-програм з [відкритим вихідним кодом](https://github.com/jrsoftware/issrc).
