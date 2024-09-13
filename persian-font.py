import tkinter as tk
from tkinter import messagebox



persian_hex_codes = {

    "ب": {'initial': '0x5A', 'medial': '0x5B', 'final': '0x59', 'isolated': '0x14'},
    "پ": {'initial': '0x42', 'medial': '0x43', 'final': '0x41', 'isolated': '0x3B'},
    "ت": {'initial': '0x5D', 'medial': '0x5E', 'final': '0x5C', 'isolated': '0x15'},
    "ث": {'initial': '0x60', 'medial': '0x61', 'final': '0x5F', 'isolated': '0x16'},
    "ج": {'initial': '0x63', 'medial': '0x64', 'final': '0x62', 'isolated': '0x17'},
    "چ": {'initial': '0x45', 'medial': '0x46', 'final': '0x44', 'isolated': '0x3C'},
    "ح": {'initial': '0x66', 'medial': '0x67', 'final': '0x65', 'isolated': '0x18'},
    "خ": {'initial': '0x69', 'medial': '0x6A', 'final': '0x68', 'isolated': '0x19'},
    "د": {'initial': '0x1A', 'medial': '0x6B', 'final': '0x6B', 'isolated': '0x1A'},
    "ذ": {'initial': '0x1B', 'medial': '0x6C', 'final': '0x6C', 'isolated': '0x1B'},
    "ر": {'initial': '0x1C', 'medial': '0x6D', 'final': '0x6D', 'isolated': '0x1C'},
    "ز": {'initial': '0x1D', 'medial': '0x6E', 'final': '0x6E', 'isolated': '0x1D'},
    "ژ": {'initial': '0x3D', 'medial': '0x47', 'final': '0x47', 'isolated': '0x3D'},
    "س": {'initial': '0x70', 'medial': '0x71', 'final': '0x6F', 'isolated': '0x1E'},
    "ش": {'initial': '0x73', 'medial': '0x74', 'final': '0x72', 'isolated': '0x1F'},
    "ص": {'initial': '0x76', 'medial': '0x77', 'final': '0x93', 'isolated': '0x20'},
    "ض": {'initial': '0x79', 'medial': '0x7A', 'final': '0x78', 'isolated': '0x21'},
    "ط": {'initial': '0x7C', 'medial': '0x7D', 'final': '0x7B', 'isolated': '0x22'},
    "ظ": {'initial': '0x7F', 'medial': '0x80', 'final': '0x7E', 'isolated': '0x23'},
    "ع": {'initial': '0x82', 'medial': '0x83', 'final': '0x81', 'isolated': '0x24'},
    "غ": {'initial': '0x85', 'medial': '0x86', 'final': '0x84', 'isolated': '0x25'},
    "ف": {'initial': '0x88', 'medial': '0x89', 'final': '0x87', 'isolated': '0x27'},
    "ق": {'initial': '0x8B', 'medial': '0x8C', 'final': '0x8A', 'isolated': '0x28'},
    "ک": {'initial': '0x49', 'medial': '0x4A', 'final': '0x48', 'isolated': '0x3E'},
    "گ": {'initial': '0x4C', 'medial': '0x4D', 'final': '0x4B', 'isolated': '0x3F'},
    "ل": {'initial': '0x8E', 'medial': '0x8F', 'final': '0x8D', 'isolated': '0x2A'},
    "م": {'initial': '0x91', 'medial': '0x92', 'final': '0x90', 'isolated': '0x2B'},
    "ن": {'initial': '0x94', 'medial': '0x95', 'final': '0x93', 'isolated': '0x2C'},
    "و": {'initial': '0x2E', 'medial': '0x97', 'final': '0x97', 'isolated': '0x2E'},
    "ه": {'initial': '0x40', 'medial': '0x4E', 'final': '0x96', 'isolated': '0x2D'},
    "ی": {'initial': '0x50', 'medial': '0x51', 'final': '0x4F', 'isolated': '0x2F'},
    "ئ": {'initial': '0x55', 'medial': '0x56', 'final': '0x54', 'isolated': '0x12'},
    "أ": {'initial': '0x10', 'medial': '0x52', 'final': '0x10', 'isolated': '0x10'},
    "ؤ": {'initial': '0x11', 'medial': '0x53', 'final': '0x11', 'isolated': '0x11'},
    "ا": {'initial': '0x13', 'medial': '0x58', 'final': '0x58', 'isolated': '0x13'},
    "آ" : "0x0F",
    "۰": "0x30",
    "۱": "0x31",
    "۲": "0x32",
    "۳": "0x33",
    "۴": "0x34",
    "۵": "0x35",
    "۶": "0x36",
    "۷": "0x37",
    "۸": "0x38",
    "۹": "0x39",
    "0": "0x30",
    "1": "0x31",
    "2": "0x32",
    "3": "0x33",
    "4": "0x34",
    "5": "0x35",
    "6": "0x36",
    "7": "0x37",
    "8": "0x38",
    "9": "0x39",
    " ": "0x0C",
    "ء": "0x0E",
    "؟": "0x0D",
    "/": "0x3A",
    ".": "0x26",
}


def convert_to_hex(persian_text):

    hex_codes = []
    length = len(persian_text)

    for i, letter in enumerate(persian_text):
        if letter not in persian_hex_codes:
            continue

        letter_data = persian_hex_codes[letter]

        if isinstance(letter_data, dict):
            if i == 0:
                if length == 1:
                    hex_codes.append(letter_data['isolated'])
                elif i < length - 1 and persian_text[i + 1] in "رزژودذئا۰۱۲۳۴۵۶۷۸۹ ؟ءآ":
                    hex_codes.append(letter_data['initial'])
                else:
                    hex_codes.append(letter_data['initial'])

            elif i == length - 1:
                if persian_text[i - 1] in "رزژودذئا۰۱۲۳۴۵۶۷۸۹ ؟ءآ":
                    hex_codes.append(letter_data['isolated'])
                else:
                    hex_codes.append(letter_data['final'])

            else:
                if persian_text[i - 1] in "رزژودذئا۰۱۲۳۴۵۶۷۸۹ ؟ءآ":
                    hex_codes.append(letter_data['initial'])
                else:
                    hex_codes.append(letter_data['medial'])

        else:
            hex_codes.append(letter_data)

    return hex_codes

def convert_hex_to_persian(hex_codes):
    persian_text = ""
    
    for hex_code in hex_codes:
        found = False
       
        for letter, data in persian_hex_codes.items():
            if isinstance(data, dict):
                for form, hex_value in data.items():
                    if hex_code == hex_value:
                        persian_text += letter
                        found = True
                        break
            else:
                if hex_code == data:
                    persian_text += letter
                    found = True
                    break
            if found:
                break
                
    return persian_text

# persian_text = "میکروکنترلر"
# hex_result = convert_to_hex(persian_text)
# persian_result = convert_hex_to_persian(hex_result)

# print("Hex Output:", hex_result)
# print("Persian Output:", persian_result)

def create_ui():
    window = tk.Tk()
    window.title("تبدیل متن به هگز و برعکس")
    font = ("B Nazanin", 12)
    


    label = tk.Label(window, text="متن فارسی", anchor="w", font=font)
    label.pack()

    input_text = tk.Entry(window, width=70, justify='right', font=font) 
    input_text.pack()

    
    hex_label = tk.Label(window, text="کد هگز", anchor="w", font=font)
    hex_label.pack()

    hex_output = tk.Text(window, height=5, width=70, font=("Times New Roman", 12))
    hex_output.tag_configure('left', justify='left')  
    hex_output.pack()
    def copy_hex_to_clipboard():
        hex_text = hex_output.get("1.0", tk.END)  
        window.clipboard_clear()  
        window.clipboard_append(hex_text)  
        window.update() 

    copy_button = tk.Button(window, text="کپی کردن هگز", command=copy_hex_to_clipboard, font=font)
    copy_button.pack()

    
    persian_label = tk.Label(window, text="متن تبدیل شده از هگز", anchor="w", font=font)
    persian_label.pack()

    persian_output = tk.Text(window, height=5, width=70, font=font)
    persian_output.tag_configure('right', justify='right') 
    persian_output.pack()

    
    def process_conversion():
        persian_text = input_text.get()

        persian_text = persian_text.replace('ي', 'ی')
        
        if not persian_text:
            messagebox.showerror("خطا", "لطفاً یک متن وارد کنید")
            return

        hex_result = convert_to_hex(persian_text)
        hex_output.delete(1.0, tk.END)

        hex_output.insert(tk.END, f"{{{', '.join(hex_result)}, 0x00}}", 'right')



        persian_result = convert_hex_to_persian(hex_result)
        persian_output.delete(1.0, tk.END)
        persian_output.insert(tk.END, persian_result, 'right')

    
    process_button = tk.Button(window, text="تبدیل", command=process_conversion, font=font)
    process_button.pack()



    
    window.mainloop()


create_ui()
