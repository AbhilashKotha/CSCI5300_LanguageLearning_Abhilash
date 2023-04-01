---
title: "Mini Project - Notes and Todo Manager"
date: 2023-03-31
---

After learning for six weeks and a short break, it's time for a mini project. We were asked to scope the project such that it is not a lot of work for the limited time available and we did just that.

We developed Notes and Todos manager application as part of the project using the tkinter library in python.

Here are the features 

- **Notes**:
  - Add quick and short notes.  
  - View, Modify and delete notes
- **Todos**:
  - Add items to the to-do list
  - View, Modify and delete items from the to-do list
  - Add a due date to the to-do item

Below are the screenshots of the application. 

![image](https://user-images.githubusercontent.com/113061137/229258547-8f4bfe93-ee17-46bb-b2b0-00863253186c.png)
![image](https://user-images.githubusercontent.com/113061137/229258554-b06e6051-55fc-4420-8aa7-c0e1a3822e96.png)


What are my major learnings from this exercise?

- I have always used Github as a code repository and even for automation of release tasks but this is the first time I am using Github issues feature. It is a feature that allows us to easily plan and complete actions for all the team members without using any external tools. 
- <code>Tkinter</code>: Though I have used Tkinter library in past for learning exercises, this time it was good learning working on multiple tabs. 
  
- SQLite: I have good knowledge on MS SQL but never used SQLite. I felt stupid for not knowing how simple SQLite is to use with python applications. 

What were the challenges then?

- There were not many challenges with the technical implementation but we faced challenges in collaboration due to different class schedules of the team members. We managed to get it done at the end though.

- For the UI design, there were not many customization options available in Tkinter library. We did not find them at least.
- In addition to these, I also faced issues in handling the input fields. For example, While accessing the text of the input field, I was getting braces { } around the text. I had to then use rstrip to exclude them Below is the code for the same.

```python

      def edit_note(self):
        selection = self.note_listbox.curselection()
        note = Note(self.db_name)
        button_text = self.edit_note_button.cget('text')
        if selection:
            note_id = self.note_listbox.get(selection[0])[0]
            text = (note.get_by_id(note_id))[0]
            note_text = self.note_entry.get('1.0', 'end-1c').rstrip()
            note.update(note_id, note_text)
            self.note_entry.delete("1.0", "end")
            self.load_notes()
```

What can we improve next?

- One thing that definitely needs improvement is decoupling the code more efficiently. Current design has the database operations also part of the notes and todo modules which can be moved to a different module.

- Defining the scope of work so that every team member gets enough work to complete before the due date.



<code>from django.contrib.auth</code>
<a href="https://github.com/AbhilashKotha/CSCI5300_LanguageLearning_Abhilash/blob/main/PythonFiles/week5\firstWebapplicationWithDjango/authentication/templates/authentication/signup.html">HTML page</a> 

