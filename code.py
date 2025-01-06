import tkinter as tk
import sqlite3
from datetime import datetime, timedelta
import os

def create_main_gui():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    global db_path
    db_path = os.path.join(script_dir, "dataproject.db")

    root = tk.Tk()
    root.title("<<ΒΕΝΖΙΝΑΔΙΚΑ ΒΛΑΧΟΣ ΑΕ>>")
    root.geometry("850x400")

    y_position = 60
    x_position = 100
    buttons = [ '1)Eισαγωγή Νέου Καταστήματος',
                "2)Eισαγωγή Νέας Δεξαμενής σε Υπάρχων Κατάστημα",
                "3)Eισαγωγή Εργαζόμενου",
                "4)Eισαγωγή Συμβόλαιου Εργαζόμενου",
                "5)Άλλαξε τιμή καυσίμου",
                "6)Eισαγωγή Αγοράς(Προσομοίωση)",
                "7)Yπολογισε Αριθμό Πωλήσεων Πρατηρίων(Μήνα)",
                "8)Υπολόγισε Αριθμό Πωλήσεων Πρατηρίων(Χρόνο)",
                "9)Υπολόγισε Αριθμό Πωλήσεων Πρατηρίων(Μέρα)",
                "10)Τζίρος Πρατηρίων συγκεκριμένη Ημέρα",
                "11)Τζίρος Πρατηρίων συγκεκριμένο Μήνα",
                "12)Τζίρος Πρατηρίων συγκεκριμένο Έτος",
                "13)Βρες Δεξαμενές κάτω από κάποιο ποσοστό",
                "14)Στατιστικά Αγορών Καυσίμων ανά Ημέρα",
                "15)Στατιστικά Αγορών Καυσίμων ανά Μήνα",
                "16)Στατιστικά Αγορών Καυσίμων ανά Έτος",
                "17)Eύρεση Κοντινών λήξεων συμβολέων"]    
    
    button_functions = [ button1,
                button2,
                button3,
                button4,
                button5,
                button6,
                button7,
                button8,
                button9,
                button10,
                button11,
                button12,
                button13,
                button14,
                button15,
                button16,
                button17]

    label = tk.Label(root, text="Επιλογή εντολής για επεξεργασία και αναζήτηση στην Βάση Δεδομένων της εταιρίας:", font=("Arial", 16), fg="blue")
    for i in range(17):
        button = tk.Button(root, text=buttons[i], width=40, height=1,bg="lightyellow", fg="red", command = button_functions[i])  
        button.place(x=x_position, y=y_position) 
        y_position = y_position+30
        if y_position == 330:
            x_position = x_position + 350
            y_position = 60
     
    label.place(x=20,y=5)


    root.mainloop()


#ΒUTTON 1

def button1():
    root = tk.Tk()
    root.title("Εισαγωγή Νέου Καταστήματος")
    root.geometry("500x500")
    
    label_age = tk.Label(root, text="Πόλη:")
    label_age.pack()
    global entry_poli
    entry_poli = tk.Entry(root)
    entry_poli.pack()
    
    label_diefthinsi = tk.Label(root, text="Διεύθυνση:")
    label_diefthinsi.pack()
    global entry_diefthinsi
    entry_diefthinsi = tk.Entry(root)
    entry_diefthinsi.pack()
    
    label_tilefwno = tk.Label(root, text="Τηλέφωνο:")
    label_tilefwno.pack()
    global entry_tilefwno
    entry_tilefwno = tk.Entry(root)
    entry_tilefwno.pack()
    
    label_wres_leitourgias = tk.Label(root, text="Ώρες Λειτουργίας:")
    label_wres_leitourgias.pack()
    global entry_wres_leitourgias
    entry_wres_leitourgias = tk.Entry(root)
    entry_wres_leitourgias.pack()
  
    insert_button = tk.Button(root, text="Insert", command=insert1)
    insert_button.pack(pady=20)
    
    global result_label
    result_label = tk.Label(root, text="")
    result_label.pack()

def insert1():
    poli = entry_poli.get()
    diefthinsi = entry_diefthinsi.get()
    tilefwno = entry_tilefwno.get()
    wres_leitourgias = entry_wres_leitourgias.get()
    
    if not poli or not diefthinsi or not tilefwno:
        result_label.config(text="Δεν έχεις βάλει αρκετά στοιχεία...", fg="red")
        return
    
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO PRATIRIO (poli, diefthinsi, tilefwno, wres_leitourgias)
                 VALUES (?, ?, ?, ?)''', (poli, diefthinsi, tilefwno, wres_leitourgias))
    connection.commit()
    connection.close()
    
    result_label.config(text="Η καταχώριση στη βάση δεδομένων ήταν επιτυχής!", fg="green")
    
    entry_poli.delete(0, tk.END)
    entry_diefthinsi.delete(0, tk.END)
    entry_tilefwno.delete(0, tk.END)
    entry_wres_leitourgias.delete(0, tk.END)



#BUTTON 2

def button2():
    root = tk.Tk()
    root.title("Εισαγωγή Nέας Δεξαμενής σε Υπάρχων Πρατήριο")
    root.geometry("500x500")
    
    label_ID_Pratiriou = tk.Label(root, text="Id του πρατηρίου:")
    label_ID_Pratiriou.pack()
    global entry_ID_Pratiriou
    entry_ID_Pratiriou = tk.Entry(root)
    entry_ID_Pratiriou.pack()
    
    label_eidos_kausimou = tk.Label(root, text="Id καυσίμου:")
    label_eidos_kausimou.pack()
    global entry_eidos_kausimou
    entry_eidos_kausimou = tk.Entry(root)
    entry_eidos_kausimou.pack()
    
    label_xwritikotita = tk.Label(root, text="Μέγιστη Χωρητικότητα σε Λίτρα:")
    label_xwritikotita.pack()
    global entry_xwritikotita
    entry_xwritikotita = tk.Entry(root)
    entry_xwritikotita.pack()
    
    label_trexousa_posotita = tk.Label(root, text="Tρέχουσα Ποσότητα:")
    label_trexousa_posotita.pack()
    global entry_trexousa_posotita
    entry_trexousa_posotita = tk.Entry(root)
    entry_trexousa_posotita.pack()
  
    insert_button = tk.Button(root, text="Insert", command=insert2)
    insert_button.pack(pady=20)
    
    global result_label
    result_label = tk.Label(root, text="")
    result_label.pack()

def insert2():
    ID_PratirioU = entry_ID_Pratiriou.get()
    eidos_kausimou = entry_eidos_kausimou.get()
    xwritikotita = entry_xwritikotita.get()
    trexousa_posotita = entry_trexousa_posotita.get()
    
    if not trexousa_posotita or not xwritikotita or not eidos_kausimou or not ID_PratirioU:
        result_label.config(text="Δεν έχεις βάλει αρκετά στοιχεία...", fg="red")
        return
    
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO DEKSAMENI (trexousa_posotita, xwritikotita, eidos_kausimou, ID_Pratiriou)
                 VALUES (?, ?, ?, ?)''', (trexousa_posotita, xwritikotita, eidos_kausimou, ID_PratirioU))
    connection.commit()
    connection.close()
    
    result_label.config(text="Η καταχώριση στη βάση δεδομένων ήταν επιτυχής!", fg="green")
    
    entry_ID_Pratiriou.delete(0, tk.END)
    entry_eidos_kausimou.delete(0, tk.END)
    entry_trexousa_posotita.delete(0, tk.END)
    entry_xwritikotita.delete(0, tk.END)


#BUTTON3

def button3():
    root = tk.Tk()
    root.title("Εισαγωγή Eργαζομένου")
    root.geometry("500x500")
    
    label_ID_ergazomenou = tk.Label(root, text="ΑΦΜ:")
    label_ID_ergazomenou.pack()
    global entry_ID_ergazomenou
    entry_ID_ergazomenou= tk.Entry(root)
    entry_ID_ergazomenou.pack()
    
    label_onoma_ergazomenou = tk.Label(root, text="Όνομα:")
    label_onoma_ergazomenou.pack()
    global entry_onoma_ergazomenou
    entry_onoma_ergazomenou = tk.Entry(root)
    entry_onoma_ergazomenou.pack()
    
    label_epwnimo_ergazomenou = tk.Label(root, text="Επώνυμο:")
    label_epwnimo_ergazomenou.pack()
    global entry_epwnimo_ergazomenou
    entry_epwnimo_ergazomenou = tk.Entry(root)
    entry_epwnimo_ergazomenou.pack()
    
    label_thesi = tk.Label(root, text="Θέση:")
    label_thesi.pack()
    global entry_thesi
    entry_thesi = tk.Entry(root)
    entry_thesi.pack()

    label_tilefwno_ergazomenou = tk.Label(root, text="Tηλέφωνο:")
    label_tilefwno_ergazomenou.pack()
    global entry_tilefwno_ergazomenou
    entry_tilefwno_ergazomenou = tk.Entry(root)
    entry_tilefwno_ergazomenou.pack()

    label_email_ergazomenou = tk.Label(root, text="email:")
    label_email_ergazomenou.pack()
    global entry_email_ergazomenou
    entry_email_ergazomenou = tk.Entry(root)
    entry_email_ergazomenou.pack()

    label_wres_ergasias = tk.Label(root, text="Eβδομαδιαίες ώρες Εργασίας:")
    label_wres_ergasias.pack()
    global entry_wres_ergasias
    entry_wres_ergasias = tk.Entry(root)
    entry_wres_ergasias.pack()

    label_ID_Pratiriou = tk.Label(root, text="ID Πρατηρίου:")
    label_ID_Pratiriou.pack()
    global entry_ID_Pratiriou
    entry_ID_Pratiriou = tk.Entry(root)
    entry_ID_Pratiriou.pack()
  
    insert_button = tk.Button(root, text="Insert", command=insert3)
    insert_button.pack(pady=20)
    
    global result_label
    result_label = tk.Label(root, text="")
    result_label.pack()

def insert3():
    ID_ergazomenou = entry_ID_ergazomenou.get()
    onoma_ergazomenou = entry_onoma_ergazomenou.get()
    epwnimo_ergazomenou = entry_epwnimo_ergazomenou.get()
    wres_ergasias = entry_wres_ergasias.get()
    thesi = entry_thesi.get()
    tilefwno_ergazomenou = entry_tilefwno_ergazomenou.get()
    email_ergazomenou = entry_email_ergazomenou.get()
    ID_pratiriou = entry_ID_Pratiriou.get()

    if not ID_ergazomenou or not onoma_ergazomenou or not epwnimo_ergazomenou or not wres_ergasias or not thesi or not tilefwno_ergazomenou or not email_ergazomenou or not ID_pratiriou:
        result_label.config(text="Δεν έχεις βάλει αρκετά στοιχεία...", fg="red")
        return
    
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        cursor.execute("SELECT ID_pratiriou FROM PRATIRIO")
        rows = cursor.fetchall()
        column_values = [row[0] for row in rows] 
    
        if int(ID_pratiriou) not in column_values:
            result_label.config(text="Δεν υπάρχει πρατήριο με τέτοιο ID", fg="red")
            return

        cursor.execute('''INSERT INTO ERGAZOMENOS (AFM_ergazomenou, onoma, epwnimo, thesi, tilefwno, e_mail, wres_ergasias, ID_pratiriou)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                       (ID_ergazomenou, onoma_ergazomenou, epwnimo_ergazomenou, thesi, tilefwno_ergazomenou, email_ergazomenou, wres_ergasias, ID_pratiriou))
        connection.commit()
        result_label.config(text="Η καταχώριση στη βάση δεδομένων ήταν επιτυχής!", fg="green")

        entry_ID_ergazomenou.delete(0, tk.END)
        entry_onoma_ergazomenou.delete(0, tk.END)
        entry_epwnimo_ergazomenou.delete(0, tk.END)
        entry_wres_ergasias.delete(0, tk.END)
        entry_thesi.delete(0, tk.END)
        entry_tilefwno_ergazomenou.delete(0, tk.END)
        entry_email_ergazomenou.delete(0, tk.END)
        entry_ID_Pratiriou.delete(0, tk.END)

    except ValueError:
        result_label.config(text="Μη έγκυρη μορφή ID ή άλλων αριθμητικών δεδομένων", fg="red")
    except sqlite3.Error as e:
        result_label.config(text=f"Σφάλμα ΒΔ: {e}", fg="red")
    finally:
        connection.close()



#BUTTON4


def button4():
    root = tk.Tk()
    root.title("Δημιουργία Συμβολαίου Εργαζομένου")
    root.geometry("500x500")
    
    label_enarksi = tk.Label(root, text="Ημερομηνία Έναρξης (μορφής ΥΥΥΥ-ΜΜ-DD):")
    label_enarksi.pack()
    global entry_enarksi
    entry_enarksi = tk.Entry(root)
    entry_enarksi.pack()
    
    label_liksi= tk.Label(root, text="Ημερομηνία Λήξης (μορφής ΥΥΥΥ-ΜΜ-DD):")
    label_liksi.pack()
    global entry_liksi
    entry_liksi = tk.Entry(root)
    entry_liksi.pack()
    
    label_misthos= tk.Label(root, text="Μισθός:")
    label_misthos.pack()
    global entry_misthos
    entry_misthos = tk.Entry(root)
    entry_misthos.pack()

    label_AFM_ergazomenou = tk.Label(root, text="ΑΦΜ Εργαζόμενου:")
    label_AFM_ergazomenou.pack()
    global entry_AFM_ergazomenou
    entry_AFM_ergazomenou = tk.Entry(root)
    entry_AFM_ergazomenou.pack()
  
    insert_button = tk.Button(root, text="Insert", command=insert4)
    insert_button.pack(pady=20)
    
    global result_label
    result_label = tk.Label(root, text="")
    result_label.pack()

def insert4():
    AFM_ergazomenou = entry_AFM_ergazomenou.get()
    enarksi = entry_enarksi.get()
    liksi = entry_liksi.get()
    misthos = entry_misthos.get()

    if not AFM_ergazomenou or not enarksi or not liksi or not misthos:
        result_label.config(text="Δεν έχεις βάλει αρκετά στοιχεία...", fg="red")
        return
    
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        cursor.execute("SELECT AFM_ergazomenou FROM ERGAZOMENOS")
        rows = cursor.fetchall()
        column_values = [row[0] for row in rows] 

        if AFM_ergazomenou not in column_values:
            result_label.config(text="Δεν υπάρχει εργαζόμενος με τέτοιο ΑΦΜ", fg="red")
            return

        cursor.execute('''INSERT INTO SYMBOLAIO (enarksi, liksi, misthos, AFM_ergazomenou)
                          VALUES (?, ?, ?, ?)''',
                       (enarksi, liksi, misthos, AFM_ergazomenou))
        connection.commit()
        result_label.config(text="Η καταχώριση στη βάση δεδομένων ήταν επιτυχής!", fg="green")

        entry_enarksi.delete(0, tk.END)
        entry_liksi.delete(0, tk.END)
        entry_misthos.delete(0, tk.END)
        entry_AFM_ergazomenou.delete(0, tk.END)
        

    except ValueError:
        result_label.config(text="Μη έγκυρη μορφή ID ή άλλων αριθμητικών δεδομένων", fg="red")
    except sqlite3.Error as e:
        result_label.config(text=f"Σφάλμα ΒΔ: {e}", fg="red")
    finally:
        connection.close()


#BUTTON 5


def button5():
    root = tk.Tk()
    root.title("Άλλαξε τιμή καυσίμου")
    root.geometry("500x500")

    label_eidos_kausimou = tk.Label(root, text="ID Καυσίμου:")
    label_eidos_kausimou.pack()
    global entry_eidos_kausimou
    entry_eidos_kausimou = tk.Entry(root)
    entry_eidos_kausimou.pack()

    label_new_price = tk.Label(root, text="Νέα Τιμή Καυσίμου:")
    label_new_price.pack()
    global entry_new_price
    entry_new_price = tk.Entry(root)
    entry_new_price.pack()

    update_button = tk.Button(root, text="Αλλαγή Τιμής", command=update_fuel_price)
    update_button.pack(pady=20)

    global result_label
    result_label = tk.Label(root, text="")
    result_label.pack()

def update_fuel_price():
    eidos_kausimou = entry_eidos_kausimou.get()
    new_price = entry_new_price.get()

    if not eidos_kausimou or not new_price:
        result_label.config(text="Παρακαλώ συμπληρώστε όλα τα πεδία.", fg="red")
        return

    try:
        new_price = float(new_price) 
    except ValueError:
        result_label.config(text="Η νέα τιμή πρέπει να είναι αριθμός.", fg="red")
        return

    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        cursor.execute("SELECT ID FROM KAFSIMO WHERE ID = ?", (eidos_kausimou,))
        if cursor.fetchone() is None:
            result_label.config(text="Το ID καυσίμου δεν υπάρχει στη βάση δεδομένων.", fg="red")
            return
        
        cursor.execute("UPDATE KAFSIMO SET timi = ? WHERE ID = ?", (new_price, eidos_kausimou))
        connection.commit()

        result_label.config(text="Η τιμή καυσίμου ενημερώθηκε επιτυχώς!", fg="green")

        entry_eidos_kausimou.delete(0, tk.END)
        entry_new_price.delete(0, tk.END)

    except sqlite3.Error as e:
        result_label.config(text=f"Σφάλμα ΒΔ: {e}", fg="red")
    finally:
        connection.close()


#BUTTON 6

def button6():
    root = tk.Tk()
    root.title("Καταχώρησε μια αγορά")
    root.geometry("500x500")

    label_eidos_kausimou = tk.Label(root, text="ID Καυσίμου:")
    label_eidos_kausimou.pack()
    global entry_eidos_kausimou
    entry_eidos_kausimou = tk.Entry(root)
    entry_eidos_kausimou.pack()

    label_ID_pratiriou = tk.Label(root, text="ID Πρατηρίου:")
    label_ID_pratiriou.pack()
    global entry_ID_pratiriou
    entry_ID_pratiriou = tk.Entry(root)
    entry_ID_pratiriou.pack()

    label_Posotita = tk.Label(root, text="Ποσότητα(Σε Λίτρα):")
    label_Posotita.pack()
    global entry_Posotita
    entry_Posotita = tk.Entry(root)
    entry_Posotita.pack()

    label_Imerominia = tk.Label(root, text="Ημερομηνία:")
    label_Imerominia.pack()
    global entry_Imerominia
    entry_Imerominia= tk.Entry(root)
    entry_Imerominia.pack()

    update_button = tk.Button(root, text="Insert", command=insert6)
    update_button.pack(pady=20)

    global result_label
    result_label = tk.Label(root, text="")
    result_label.pack()

def insert6():
    eidos_kausimou = entry_eidos_kausimou.get()
    ID_pratiriou = entry_ID_pratiriou.get()
    Posotita = entry_Posotita.get()
    Imerominia = entry_Imerominia.get()

    if not eidos_kausimou or not ID_pratiriou or not Posotita or not Imerominia:
        result_label.config(text="Δεν έχεις βάλει αρκετά στοιχεία...", fg="red")
        return

    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # Validate eidos_kausimou (check if the fuel ID exists)
        cursor.execute("SELECT ID FROM KAFSIMO")
        eidos_kausimou_values = [row[0] for row in cursor.fetchall()]
        if int(eidos_kausimou) not in eidos_kausimou_values:
            result_label.config(text="Δεν υπάρχει καύσιμο με τέτοιο ID", fg="red")
            return

        # Validate ID_pratiriou (check if the station ID exists)
        cursor.execute("SELECT ID_pratiriou FROM PRATIRIO")
        pratiriou_values = [row[0] for row in cursor.fetchall()]
        if int(ID_pratiriou) not in pratiriou_values:
            result_label.config(text="Δεν υπάρχει πρατήριο με τέτοιο ID", fg="red")
            return

        # Fetch Timi (price) for the selected fuel
        cursor.execute("SELECT Timi FROM KAFSIMO WHERE ID = ?", (int(eidos_kausimou),))
        result = cursor.fetchone()

        if not result or result[0] is None:
            result_label.config(text="Δεν βρέθηκε τιμή για το καύσιμο", fg="red")
            return
        
        Timi = result[0]

        # Ensure Timi is a valid float
        try:
            Timi = float(Timi)
        except ValueError:
            result_label.config(text="Η τιμή του καυσίμου δεν είναι έγκυρη", fg="red")
            return

        # Validate Posotita (quantity)
        try:
            Posotita = int(Posotita)
        except ValueError:
            result_label.config(text="Η ποσότητα πρέπει να είναι αριθμός", fg="red")
            return

        # Calculate poso_plirwmis (total cost)
        poso_plirwmis = Posotita * Timi

        # Insert the data into the AGORA table
        cursor.execute('''INSERT INTO AGORA (Posotita, Imerominia, ID_pratiriou, ID_kausimou, poso_plirwmis)
                          VALUES (?, ?, ?, ?, ?)''',
                       (Posotita, Imerominia, ID_pratiriou, eidos_kausimou, poso_plirwmis))
        connection.commit()

        result_label.config(text="Η καταχώριση στη βάση δεδομένων ήταν επιτυχής!", fg="green")

        # Clear inputs
        entry_eidos_kausimou.delete(0, tk.END)
        entry_Imerominia.delete(0, tk.END)
        entry_ID_pratiriou.delete(0, tk.END)
        entry_Posotita.delete(0, tk.END)

    except sqlite3.Error as e:
        result_label.config(text=f"Σφάλμα ΒΔ: {e}", fg="red")
    finally:
        connection.close()




#BUTTON 7

def button7():
    root = tk.Tk()
    root.title("c")
    root.geometry("500x500")
    
    label_minas = tk.Label(root, text="Εισαγωγή Μήνα(Μορφής ΥΥΥΥ-MM)")
    label_minas.pack()
    global entry_minas
    entry_minas = tk.Entry(root)
    entry_minas.pack()
  
    insert_button = tk.Button(root, text="Insert", command=insert7)
    insert_button.pack(pady=20)
    
    global result_label
    result_label = tk.Label(root, text="")
    result_label.pack()

def insert7():
    minas = entry_minas.get()

    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        cursor.execute("SELECT ID_pratiriou FROM PRATIRIO")
        ids = cursor.fetchall()

        synola = [0] * len(ids)

        for i in range(len(ids)):
            id_pratiriou = ids[i][0]
            cursor.execute(
                "SELECT COUNT(*) FROM AGORA WHERE ID_pratiriou = ? AND Imerominia LIKE ?",
                (id_pratiriou, f"{minas}-%") 
            )
            synola[i] = cursor.fetchone()[0]

        result_text = "\n".join([f"Πρατήριο {ids[i][0]}: {synola[i]} πωλήσεις" for i in range(len(ids))])
        result_label.config(text=result_text, fg="green")

        entry_minas.delete(0, tk.END)

    except Exception as e:
        result_label.config(text=f"Σφάλμα: {str(e)}", fg="red")

    finally:
        connection.close()


#BUTTON 8


def button8():

    root = tk.Tk()
    root.title("c")
    root.geometry("500x500")
    
    label_etos = tk.Label(root, text="Εισαγωγή Έτους(Μορφής ΥΥΥΥ)")
    label_etos.pack()
    global entry_etos
    entry_etos = tk.Entry(root)
    entry_etos.pack()
  
    insert_button = tk.Button(root, text="Insert", command=insert8)
    insert_button.pack(pady=20)
    
    global result_label
    result_label = tk.Label(root, text="")
    result_label.pack()


def insert8():
    etos = entry_etos.get()  

    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        cursor.execute("SELECT ID_pratiriou FROM PRATIRIO")
        ids = cursor.fetchall()

        synola = [0] * len(ids)

        for i in range(len(ids)):
            id_pratiriou = ids[i][0]
            cursor.execute(
                "SELECT COUNT(*) FROM AGORA WHERE ID_pratiriou = ? AND Imerominia LIKE ?",
                (id_pratiriou, f"{etos}-%")
            )
            synola[i] = cursor.fetchone()[0]

        result_text = "\n".join([f"Πρατήριο {ids[i][0]}: {synola[i]} πωλήσεις" for i in range(len(ids))])
        result_label.config(text=result_text, fg="green")

        entry_etos.delete(0, tk.END)

    except Exception as e:
        result_label.config(text=f"Σφάλμα: {str(e)}", fg="red")

    finally:
        connection.close()


#BUTTON 9

def button9():
    
    root = tk.Tk()
    root.title("c")
    root.geometry("500x500")
    
    label_mera = tk.Label(root, text="Εισαγωγή Mέρας(Μορφής ΥΥΥΥ-ΜΜ-DD):")
    label_mera.pack()
    global entry_mera
    entry_mera = tk.Entry(root)
    entry_mera.pack()
  
    insert_button = tk.Button(root, text="Insert", command=insert9)
    insert_button.pack(pady=20)
    
    global result_label
    result_label = tk.Label(root, text="")
    result_label.pack()

def insert9():
    mera = entry_mera.get()  

    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        cursor.execute("SELECT ID_pratiriou FROM PRATIRIO")
        ids = cursor.fetchall()

        synola = [0] * len(ids)

        for i in range(len(ids)):
            id_pratiriou = ids[i][0]
            cursor.execute(
                "SELECT COUNT(*) FROM AGORA WHERE ID_pratiriou = ? AND Imerominia = ?",
                (id_pratiriou, mera)
            )
            synola[i] = cursor.fetchone()[0]

        result_text = "\n".join([f"Πρατήριο {ids[i][0]}: {synola[i]} πωλήσεις" for i in range(len(ids))])
        result_label.config(text=result_text, fg="green")

        entry_mera.delete(0, tk.END)

    except Exception as e:
        result_label.config(text=f"Σφάλμα: {str(e)}", fg="red")

    finally:
        connection.close()



#BUTTON 10


def button10():
    
    root = tk.Tk()
    root.title("c")
    root.geometry("500x500")
    
    label_mera = tk.Label(root, text="Εισαγωγή Mέρας(Μορφής ΥΥΥΥ-ΜΜ-DD):")
    label_mera.pack()
    global entry_mera
    entry_mera = tk.Entry(root)
    entry_mera.pack()
  
    insert_button = tk.Button(root, text="Insert", command=insert10)
    insert_button.pack(pady=20)
    
    global result_label
    result_label = tk.Label(root, text="")
    result_label.pack()

def insert10():
    mera = entry_mera.get()  

    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        cursor.execute("SELECT ID_pratiriou FROM PRATIRIO")
        ids = cursor.fetchall()

        synola = [0] * len(ids)

        for i in range(len(ids)):
            id_pratiriou = ids[i][0]
            cursor.execute(
                "SELECT SUM(poso_plirwmis) FROM AGORA WHERE ID_pratiriou = ? AND Imerominia = ?",
                (id_pratiriou, mera)
            )
            synola[i] = cursor.fetchone()[0]

        result_text = "\n".join([f"Το πρατήριο <<{ids[i][0]}>> είχε τζίρο {synola[i]} ευρώ." for i in range(len(ids))])
        result_label.config(text=result_text, fg="green")

        entry_mera.delete(0, tk.END)

    except Exception as e:
        result_label.config(text=f"Σφάλμα: {str(e)}", fg="red")

    finally:
        connection.close()


#BUTTON 11


def button11():
    root = tk.Tk()
    root.title("c")
    root.geometry("500x500")
    
    label_minas = tk.Label(root, text="Εισαγωγή Μήνα(Μορφής ΥΥΥΥ-MM)")
    label_minas.pack()
    global entry_minas
    entry_minas = tk.Entry(root)
    entry_minas.pack()
  
    insert_button = tk.Button(root, text="Insert", command=insert11)
    insert_button.pack(pady=20)
    
    global result_label
    result_label = tk.Label(root, text="")
    result_label.pack()

def insert11():
    minas = entry_minas.get()

    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        cursor.execute("SELECT ID_pratiriou FROM PRATIRIO")
        ids = cursor.fetchall()

        synola = [0] * len(ids)

        for i in range(len(ids)):
            id_pratiriou = ids[i][0]
            cursor.execute(
                "SELECT SUM(poso_plirwmis) FROM AGORA WHERE ID_pratiriou = ? AND Imerominia LIKE ?",
                (id_pratiriou, f"{minas}-%") 
            )
            synola[i] = cursor.fetchone()[0]

        result_text = "\n".join([f"Το πρατήριο <<{ids[i][0]}>> είχε τζίρο {synola[i]} ευρώ." for i in range(len(ids))])
        result_label.config(text=result_text, fg="green")

        entry_minas.delete(0, tk.END)

    except Exception as e:
        result_label.config(text=f"Σφάλμα: {str(e)}", fg="red")

    finally:
        connection.close()


#BUTTON 13


def button13():
    root = tk.Tk()
    root.title("c")
    root.geometry("500x500")
    
    label_pososto = tk.Label(root, text="Ποσοστό:)")
    label_pososto.pack()
    global entry_pososto
    entry_pososto = tk.Entry(root)
    entry_pososto.pack()
  
    insert_button = tk.Button(root, text="Insert", command=insert13)
    insert_button.pack(pady=20)
    
    global result_label
    result_label = tk.Label(root, text="")
    result_label.pack()

def insert13():
    try:
        pososto = float(entry_pososto.get())

        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        cursor.execute(
            "SELECT ID FROM DEKSAMENI WHERE trexousa_posotita / xwritikotita < ?", 
            (pososto / 100,)
        )
        ids = cursor.fetchall()

        id_pratiriwn = []
        addresses = []

        for i in range(len(ids)):
            
            cursor.execute(
                "SELECT ID_pratiriou FROM DEKSAMENI WHERE ID = ?", 
                (ids[i][0],)  
            )
            id_pratiriwn.append(cursor.fetchone()[0])  

            cursor.execute(
                "SELECT diefthinsi FROM PRATIRIO WHERE id_pratiriou = ?",
                (id_pratiriwn[i],)  
            )
            addresses.append(cursor.fetchone()[0]) 

        result_text = "\n".join(
            [f"H δεξαμενή {ids[i][0]} που βρίσκεται στο πρατήριο <<{id_pratiriwn[i]}>> στην οδό {addresses[i]} θέλει γέμισμα!" 
             for i in range(len(id_pratiriwn))]
        )
        
        result_label.config(text=result_text, fg="green")

        entry_pososto.delete(0, tk.END)


    except Exception as e:
        result_label.config(text=f"Σφάλμα: {str(e)}", fg="red")

    finally:
        connection.close()



#BUTTON 12


def button12():

    root = tk.Tk()
    root.title("c")
    root.geometry("500x500")
    
    label_etos = tk.Label(root, text="Εισαγωγή Έτους(Μορφής ΥΥΥΥ)")
    label_etos.pack()
    global entry_etos
    entry_etos = tk.Entry(root)
    entry_etos.pack()
  
    insert_button = tk.Button(root, text="Insert", command=insert12)
    insert_button.pack(pady=20)
    
    global result_label
    result_label = tk.Label(root, text="")
    result_label.pack()


def insert12():
    etos = entry_etos.get()  

    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        cursor.execute("SELECT ID_pratiriou FROM PRATIRIO")
        ids = cursor.fetchall()

        synola = [0] * len(ids)

        for i in range(len(ids)):
            id_pratiriou = ids[i][0]
            cursor.execute(
                "SELECT SUM(poso_plirwmis) FROM AGORA WHERE ID_pratiriou = ? AND Imerominia LIKE ?",
                (id_pratiriou, f"{etos}-%")
            )
            synola[i] = cursor.fetchone()[0]

        result_text = "\n".join([f"Το πρατήριο <<{ids[i][0]}>> είχε τζίρο {synola[i]} ευρώ." for i in range(len(ids))])
        result_label.config(text=result_text, fg="green")

        entry_etos.delete(0, tk.END)

    except Exception as e:
        result_label.config(text=f"Σφάλμα: {str(e)}", fg="red")

    finally:
        connection.close()


#BUTTON 14

def button14():
    root = tk.Tk()
    root.title("c")
    root.geometry("500x500")
    
    label_mera = tk.Label(root, text="Εισαγωγή Μέρας(Μορφής ΥΥΥΥ-MM-DD)")
    label_mera.pack()

    global entry_mera
    entry_mera = tk.Entry(root)
    entry_mera.pack()
  
    insert_button = tk.Button(root, text="Insert", command=insert14)
    insert_button.pack(pady=20)
    
    global result_label
    result_label = tk.Label(root, text="")
    result_label.pack()

def insert14():
    mera = entry_mera.get()
    synola = [] 
    onoma = []   

    try:
        connection = sqlite3.connect(db_path) 
        cursor = connection.cursor()

        for i in range(1, 6):  
            cursor.execute(
                "SELECT SUM(Posotita) FROM AGORA WHERE ID_kausimou = ? AND IMEROMINIA = ?",
                (i, mera)
            )
            result = cursor.fetchone()
            if result: 
                synola.append(result[0])  
            else:
                synola.append(0) 

            cursor.execute(
                "SELECT onoma FROM KAFSIMO WHERE ID = ?",
                (i,)
            )
            result = cursor.fetchone()
            if result:
                onoma.append(result[0]) 
            else:
                onoma.append("Unknown Fuel") 


        result_text = "\n".join([f"To καύσιμο ({onoma[i]}) είχε κατανάλωση {synola[i]} λίτρα." for i in range(len(synola))])
        result_label.config(text=result_text, fg="green")

        entry_mera.delete(0, tk.END)

    except Exception as e:
        result_label.config(text=f"Σφάλμα: {str(e)}", fg="red")

    finally:   
        connection.close()




#BUTTON 15


def button15():
    root = tk.Tk()
    root.title("c")
    root.geometry("500x500")
    
    label_minas = tk.Label(root, text="Εισαγωγή Mήνα(Μορφής ΥΥΥΥ-MM)")
    label_minas.pack()

    global entry_minas
    entry_minas = tk.Entry(root)
    entry_minas.pack()
  
    insert_button = tk.Button(root, text="Insert", command=insert15)
    insert_button.pack(pady=20)
    
    global result_label
    result_label = tk.Label(root, text="")
    result_label.pack()


def insert15():
    minas = entry_minas.get() 
    synola = []  
    onoma = []   

    try:

        connection = sqlite3.connect(db_path)  
        cursor = connection.cursor()

       
        for i in range(1, 6): 
            
            cursor.execute(
                "SELECT SUM(Posotita) FROM AGORA WHERE ID_kausimou = ? AND IMEROMINIA LIKE ?",
                (i, f"{minas}-%")
            )
            result = cursor.fetchone()
            if result and result[0] is not None: 
                synola.append(result[0])  
            else:
                synola.append(0)  

           
            cursor.execute(
                "SELECT onoma FROM KAFSIMO WHERE ID = ?",
                (i,)
            )
            result = cursor.fetchone()
            if result:  
                onoma.append(result[0]) 
            else:
                onoma.append("Unknown Fuel")  

        result_text = "\n".join([f"To καύσιμο ({onoma[i]}) είχε κατανάλωση {synola[i]} λίτρα τον μήνα {minas}." for i in range(len(synola))])
        result_label.config(text=result_text, fg="green")

        entry_minas.delete(0, tk.END)

    except Exception as e:
        result_label.config(text=f"Σφάλμα: {str(e)}", fg="red")

    finally:
        connection.close()


#BUTTON 16


def button16():

    root = tk.Tk()
    root.title("c")
    root.geometry("500x500")
    
    label_etos = tk.Label(root, text="Εισαγωγή Mήνα(Μορφής ΥΥΥΥ")
    label_etos.pack()

    global entry_etos
    entry_etos= tk.Entry(root)
    entry_etos.pack()
  
    insert_button = tk.Button(root, text="Insert", command=insert16)
    insert_button.pack(pady=20)
    
    global result_label
    result_label = tk.Label(root, text="")
    result_label.pack()



def insert16():
    etos = entry_etos.get()
    synola = [] 
    onoma = []

    try:
        connection = sqlite3.connect(db_path) 
        cursor = connection.cursor()

        for i in range(1, 6): 
            cursor.execute(
                "SELECT SUM(Posotita) FROM AGORA WHERE ID_kausimou = ? AND IMEROMINIA LIKE ?",
                (i, f"{etos}-%")  
            )
            result = cursor.fetchone()
            if result and result[0] is not None: 
                synola.append(result[0])  
            else:
                synola.append(0)  

            cursor.execute(
                "SELECT onoma FROM KAFSIMO WHERE ID = ?",
                (i,)
            )
            result = cursor.fetchone()
            if result:  
                onoma.append(result[0]) 
            else:
                onoma.append("Unknown Fuel")  


        result_text = "\n".join([f"To καύσιμο ({onoma[i]}) είχε κατανάλωση {synola[i]} λίτρα το έτος {etos}." for i in range(len(synola))])
        result_label.config(text=result_text, fg="green")

        entry_etos.delete(0, tk.END)

    except Exception as e:
        result_label.config(text=f"Σφάλμα: {str(e)}", fg="red")

    finally:
        connection.close()

#BUTTON 17


def button17():

    root = tk.Tk()
    root.title("c")
    root.geometry("500x500")
    
    label_meres = tk.Label(root, text="Για πόσες μέρες θες να δεις συμβόλαια που λήγουν:")
    label_meres.pack()

    global entry_meres
    entry_meres = tk.Entry(root)
    entry_meres.pack()
  
    insert_button = tk.Button(root, text="Insert", command=insert17)
    insert_button.pack(pady=20)
    
    global result_label
    result_label = tk.Label(root, text="")
    result_label.pack()

def insert17():
    meres = int(entry_meres.get()) 

    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        today = datetime.today()
        orio = today + timedelta(days=meres)
        today_str = today.strftime("%Y-%m-%d")
        orio_str = orio.strftime("%Y-%m-%d")

        cursor.execute("""
            SELECT E.AFM_ergazomenou, E.onoma, E.epwnimo, S.liksi
            FROM ERGAZOMENOS E
            JOIN SYMBOLAIO S ON E.AFM_ergazomenou = S.AFM_ergazomenou
            WHERE S.liksi BETWEEN ? AND ?
        """, (today_str, orio_str))

        ergazomenoi = cursor.fetchall()

        if ergazomenoi:
            result_text = "Υπάλληλοι που τους τελειώνει το συμβόλαιο:\n"
            for emp in ergazomenoi:
                result_text += f"ΑΦΜ: {emp[0]}, Ονοματεπώνυμο: {emp[1]} {emp[2]}, Λήξη Συμβολαίου: {emp[3]}\n"
            result_label.config(text=result_text, fg="green")
        else:
            result_label.config(text="Κανενός υπαλλήλου δεν του λήγει το συμβόλαιο σύντομα.", fg="blue")

    except sqlite3.Error as e:
        result_label.config(text=f"Database error: {e}", fg="red")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}", fg="red")
    finally:
        if connection:
            connection.close()


create_main_gui()

