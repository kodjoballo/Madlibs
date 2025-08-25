# 📝 Madlibs Game

## 📌 Description
The **Madlibs Game** is a fun interactive program where you take a story with missing parts (enclosed in `< >`) and fill in your own words to create a funny or unexpected story.  

For example, a story template might look like:  
```text
Today I went to the <place> and saw a <animal> that was very <adjective>.


And after filling in the blanks:

```js
Today I went to the **beach** and saw a **monkey** that was very **angry**.
```

### 🚀 How to Run
### 1. Prepare a Story File

Create a text file named madlibs_story.txt in the same directory as the program.
Example:
```js
Once upon a time, there was a <adjective> <animal> who loved to <verb> every day.
```

### 2. Run the Program

```js
python.exe madlibs.py
```

### 3. Fill in the Blanks

The program will ask you for words:

```js
Enter a word for <adjective>: funny
Enter a word for <animal>: cat
Enter a word for <verb>: dance
```


Final Output:

```js
Once upon a time, there was a funny cat who loved to dance every day.
```

### 📚 Concepts Used

File handling (reading from madlibs_story.txt)

Strings & placeholders (< >)

Sets & loops for unique word replacement

User input & dictionary mapping

### 🖼️ Screenshot
<p align="center">

![image alt](https://github.com/kodjoballo/Madlibs/blob/main/madlibs.png?raw=true)

</p>

### 💡 Ideas to Extend

Add multiple stories and let the user pick one

Randomly select a story each time

Save the completed story into a new file (madlibs_result.txt)

Create a GUI version with Tkinter

### code_source ☺️👇

[source_code](https://github.com/kodjoballo/Madlibs/blob/main/madlibs.py)


