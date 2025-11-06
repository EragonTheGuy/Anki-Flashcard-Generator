from tkinter import *
import settings

from fetch_definition import get_definition
from upload_to_anki import upload_anki, is_anki_listening, ensure_deck_exists

"""
Contains the AnkiGUI class, which builds a Tkinter-based interface for entering words,
selecting card types, and optionally including pronunciation. 
It integrates with AnkiConnect to upload the given word and definition.
"""

class AnkiGUI:
    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")
        self.root.title("Card-Creator")
        self.root.configure(background="#5b7a85")

        # Center the window
        window_width = 1300
        window_height = 750
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry("%dx%d" % (width, height))


        # ==== Entry box ====
        self.ent = Entry(root)
        self.ent.config(width=29, background="white", foreground="black",
                        borderwidth=0, bd=0, font=("Arial", 25), justify="center")
        self.ent.focus_set()

        # Place the entry box
        self.ent.place(relx=0.5, rely=0.25, anchor='center')

        # ==== Text entry box ====
        self.ent2 = Text(root)

        self.ent2.config(width=29, background="white", foreground="black",
                        borderwidth=2, font=("Arial", 25), height=4)

        # Place the text entry box
        self.ent2.place(relx=0.5, rely=0.5, anchor='center')

        self.label1 = Label(root)
        self.label1.config(text="Word", background="#5b7a85", font=("Arial", 25))
        self.label1.place(relx=0.5, rely=0.15, anchor='center')

        self.label2 = Label(root)
        self.label2.config(text="Definition", background="#5b7a85", font=("Arial", 25))
        self.label2.place(relx=0.5, rely=0.345, anchor='center')


        # ==== Status bar ====
        self.status = Label(root, text="", bd=1, anchor="w", font=("Arial", 19))
        self.status.grid(column=1, columnspan=1, row=6, sticky="w")

        # ==== Submit button ====
        submit_button = Button(root, command=self.submit, text="Submit",
                               bg="#101010", fg="white", height=2, width=30,
                               activeforeground="white", activebackground="#212121",
                               bd=0, highlightthickness=0)
        submit_button.grid(row=20, column=1, columnspan=2, pady=(15, 70))

        # Place the submit button
        submit_button.place(relx=0.5, rely=0.7, anchor='center')

        def key_handler(event):
            if event.keysym == 'Return' and self.ent2.focus_get() == ".!entry2":
                print("submitted")
                self.submit()
            elif self.ent2.focus_get() == '.!entry2':
                print("focused")
            elif event.keysym == 'Return':
                print("should not submit")
                print(self.ent2.focus_get())
                self.ent2.focus_set()

        root.bind('<Key>', key_handler)
        root.mainloop()

    def show_status(self, duration=3000):
        self.status.config(text="Done!", fg="white", bg="black")
        self.root.after(duration, lambda: self.status.config(text=""))

    def error_window(self, error_msg):
        popup_width = 350
        popup_height = 150

        popup = Toplevel(self.root)
        popup.transient(self.root)
        popup.grab_set()
        popup.title("Error")
        popup.config(bg="#080808")

        # Get root window position and size
        root_x = self.root.winfo_x()
        root_y = self.root.winfo_y()
        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()

        # Center popup relative to root window
        x = root_x + (root_width // 2) - (popup_width // 2)
        y = root_y + (root_height // 2) - (popup_height // 2)
        popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        def close_popup(event=None):
                popup.destroy()
                self.root.unbind("<Return>")
                self.ent.focus_set()

        # Create content frame
        frame = Frame(popup, bg="#080808", padx=20, pady=20)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Error message
        error_message = Label(frame, text=error_msg,
                            bg="#080808", fg="white", pady=24, font=("Arial", 12))
        error_message.pack()

        # OK button
        ok_button = Button(frame, text="OK", command=close_popup,
                        bg="#101010", fg="white", width=11,
                        activeforeground="white", activebackground="#212121",
                        bd=0, highlightthickness=0)
        ok_button.pack()

        ok_button.focus_set()
        # Bind Enter key to close the popup
        ok_button.bind("<Return>", close_popup)

    def submit(self, event=None):
        word = self.ent.get()
        card_type = "basic"
        if not word:
            return

        definition = self.ent2.get()
        if not definition:
            return

        #check if ankiConnect is on
        if not is_anki_listening():
            self.error_window("Couldn't detect AnkiConnect.")
            return

        # create a deck if not existed. Deck name : "vocabular"
        if not settings.deckExists:
            ensure_deck_exists()


        upload_anki(word, definition, card_type)

        # clear the entry box
        self.ent.delete(0, 'end')
        self.ent2.delete(0, 'end')

        #show status (done) with a one-second delay.
        self.root.after(100, self.show_status)





 
