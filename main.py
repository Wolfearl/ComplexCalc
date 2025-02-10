from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import math


def get_quarter(a, b):
    if a > 0 and b > 0:
        return 1
    if a < 0 < b:
        return 2
    if a < 0 and b < 0:
        return 3
    return 4


def create_frame(bord=None, rel=None, pad=None, h=None, w=None, m=1, n=1, b=None):
    if pad is None:
        pad = [0, 0]
    frame = Frame(borderwidth=bord, relief=rel, padx=pad[0], pady=pad[1], bg=b, width=w, height=h)
    for c in range(m):
        frame.columnconfigure(index=c, weight=1)
    for r in range(n):
        frame.rowconfigure(index=r, weight=1)
    return frame


def fill_the_windows(root):
    common_font = ("Libertine", 9, "bold")
    common_default = "(x . x) ~~zzZ"
    common_error = "(」°ロ°)」"
    start_emoji = "(⌒‿⌒)"
    happy_emoji = "o(≧▽≦)o"

#----------------------------ФОРМУЛЫ-----------------------------------
    frame_rules = create_frame(3, SOLID)
    frame_rules.pack(side=LEFT, fill=Y, expand=False)

    image_rules = Image.open('rules.png')
    photo = ImageTk.PhotoImage(image_rules)
    photo_lbl = ttk.Label(frame_rules, image=photo)
    photo_lbl.image=photo
    photo_lbl.grid()

# -----------------------------ВВОД------------------------------------
    frame_input = create_frame(bord=3, rel=SOLID, pad=[5, 5], m=5, n=2)
    frame_input.pack(anchor=NE, fill=X, padx=5, pady=5)

    # -------------------Z1-------------------
    lbl1 = ttk.Label(frame_input, text='Z1    = ', font=common_font)
    lbl1.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    ent1 = ttk.Entry(frame_input, font=common_font, width=10)
    ent1.insert(0, '1')
    ent1.grid(row=0, column=1, padx=5, pady=5)

    lbl2 = ttk.Label(frame_input, text=' + i * ', font=common_font)
    lbl2.grid(row=0, column=2, padx=5, pady=5, sticky="w")

    ent2 = ttk.Entry(frame_input, font=common_font, width=10)
    ent2.insert(0, '1')
    ent2.grid(row=0, column=3, padx=5, pady=5)

    # -------------------Z2-------------------
    lbl3 = ttk.Label(frame_input, text='Z2    = ', font=common_font)
    lbl3.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    ent3 = ttk.Entry(frame_input, font=common_font, width=10)
    ent3.insert(0, '1')
    ent3.grid(row=1, column=1, padx=5, pady=5)

    lbl4 = ttk.Label(frame_input, text=' + i * ', font=common_font)
    lbl4.grid(row=1, column=2, padx=5, pady=5, sticky="w")

    ent4 = ttk.Entry(frame_input, font=common_font, width=10)
    ent4.insert(0, '1')
    ent4.grid(row=1, column=3, padx=5, pady=5)

# -----------------------------------ПРОВЕРКА--------------------------------------
    frame_test = create_frame(bord=3, rel=SOLID, pad=[5, 5])
    frame_test.pack(anchor=S, fill=X, padx=5, pady=5)

    test_input = StringVar(value=start_emoji)
    test_lbl = ttk.Label(frame_test, textvariable=test_input, font=common_font)
    test_lbl.grid(sticky="s")


# -----------------------ПЕРВАЯ СТУПЕНЬ ВЫЧИСЛЕНИЯ---------------------------------
    frame_first_calc = create_frame(bord=3, rel=SOLID, pad=[5, 5], m=3, n=4)
    frame_first_calc.pack(anchor=S, fill=X, padx=5, pady=5)

    otv = [['Z1 + Z2', 'Z1 - Z2', 'Z1 * Z2', 'Z1 / Z2'], ['='] * 4]
    for j in range(2):
        for i in range(4):
            ttk.Label(frame_first_calc, text=otv[j][i], font=common_font).grid(row=i, column=j, sticky="s")

    sum_z = StringVar(value=common_default)
    lbl_sum_z = ttk.Label(frame_first_calc, textvariable=sum_z, font=common_font)
    lbl_sum_z.grid(row=0, column=2, sticky="s")

    diff_z = StringVar(value=common_default)
    lbl_diff_z = ttk.Label(frame_first_calc, textvariable=diff_z, font=common_font)
    lbl_diff_z.grid(row=1, column=2, sticky="s")

    mult = StringVar(value=common_default)
    lbl_mult_z = ttk.Label(frame_first_calc, textvariable=mult, font=common_font)
    lbl_mult_z.grid(row=2, column=2, sticky="s")

    div = StringVar(value=common_default)
    lbl_div_z = ttk.Label(frame_first_calc, textvariable=div, font=common_font)
    lbl_div_z.grid(row=3, column=2, sticky="s")

# --------------------------------ОБЪЯВЛЕНИЕ-------------------------------------
    frame_name_degree = create_frame(bord=3, rel=SOLID, pad=[5, 5])
    frame_name_degree.pack(anchor=S, fill=X, padx=5, pady=5)

    name_degree_lbl = ttk.Label(frame_name_degree, text='Тригонометрическая форма', font=common_font)
    name_degree_lbl.grid(sticky='s')

# -----------------------ВТОРАЯ СТУПЕНЬ ВЫЧИСЛЕНИЯ---------------------------------
    frame_trig = create_frame(bord=3, rel=SOLID, pad=[5, 5], m=3, n=4)
    frame_trig.pack(anchor=S, fill=X, padx=5, pady=5)

    otv = [['R1 = |Z1|', 'R2 = |Z2|', 'fi1', 'fi2', 'Z1 * Z2', 'Z1 / Z2', 'Z1^n', 'Z2^n'], ['='] * 8]
    for j in range(2):
        for i in range(8):
            ttk.Label(frame_trig, text=otv[j][i], font=common_font).grid(row=i, column=j, sticky="s")

    tr_r1 = StringVar(value=common_default)
    tr_r1_lbl = ttk.Label(frame_trig, textvariable=tr_r1, font=common_font)
    tr_r1_lbl.grid(row=0, column=2, sticky="s")

    tr_r2 = StringVar(value=common_default)
    tr_r2_lbl = ttk.Label(frame_trig, textvariable=tr_r2, font=common_font)
    tr_r2_lbl.grid(row=1, column=2, sticky="s")

    f1 = StringVar(value=common_default)
    f1_lbl = ttk.Label(frame_trig, textvariable=f1, font=common_font)
    f1_lbl.grid(row=2, column=2, sticky="s")

    f2 = StringVar(value=common_default)
    f2_lbl = ttk.Label(frame_trig, textvariable=f2, font=common_font)
    f2_lbl.grid(row=3, column=2, sticky="s")

    tr_mult = StringVar(value=common_default)
    tr_mult_lbl = ttk.Label(frame_trig, textvariable=tr_mult, font=common_font)
    tr_mult_lbl.grid(row=4, column=2, sticky="s")

    tr_div = StringVar(value=common_default)
    tr_div_lbl = ttk.Label(frame_trig, textvariable=tr_div, font=common_font)
    tr_div_lbl.grid(row=5, column=2, sticky="s")

    tr_deg1 = StringVar(value=common_default)
    tr_deg1_lbl = ttk.Label(frame_trig, textvariable=tr_deg1, font=common_font)
    tr_deg1_lbl.grid(row=6, column=2, sticky="s")

    tr_deg2 = StringVar(value=common_default)
    tr_deg2_lbl = ttk.Label(frame_trig, textvariable=tr_deg2, font=common_font)
    tr_deg2_lbl.grid(row=7, column=2, sticky="s")

# -----------------------ИЗМЕНЕНИЕ СТЕПЕНИ И ОКРУГЛЕНИЯ---------------------------------
    def change_degree(newVal):
        des_lbl1['text'] = f'Округление до {round(nd.get())}'

    def change_rounding(newVal):
        des_lbl2['text'] = f'Степень n = {round(n.get())}'

    frame_scale = create_frame(bord=3, rel=SOLID, pad=[2, 2], m=4)
    frame_scale.pack(anchor=S, fill=X, pady=1, padx=5)

    nd = IntVar(value=2)
    n = IntVar(value=2)

    des_lbl1 = ttk.Label(frame_scale, text = f'Округление до {nd.get()}', font=common_font)
    des_lbl1.grid(row=0, column=0, sticky="s")

    horizontalScale1 = ttk.Scale(frame_scale, orient=HORIZONTAL, length=100, from_=1.0, to=10,
                                 variable=nd, command=change_degree)
    horizontalScale1.grid(row=0, column=1, sticky="s")

    des_lbl2 = ttk.Label(frame_scale, text = f'Степень n = {n.get()}', font=common_font)
    des_lbl2.grid(row=0, column=2, sticky="s")

    horizontalScale2 = ttk.Scale(frame_scale, orient=HORIZONTAL, length=100, from_=1.0, to=10,
                                 variable=n, command=change_rounding)
    horizontalScale2.grid(row=0, column=3, sticky="s")


    def get_result():
        a = ent1.get()
        b = ent2.get()
        c = ent3.get()
        d = ent4.get()
        try:
            a, c, b, d = eval(a), eval(c), eval(b), eval(d)
            common_round = round(float(nd.get()))
            common_n = round(float(n.get()))

            test_input.set(happy_emoji)

            sum_z.set(f'{a + c} + i * {b + d}')
            diff_z.set(f'{(a - c)} + i * {b - d}')
            mult.set(f'{a * c - b * d} + i * {a * d + b * c}')
            div.set(f'{(a * c + b * d) / (c * c + d * d):.{common_round}} + i * {(b * c - a * d) / (c * c + d * d):.{common_round}}')

            #Тригонометрия
            r1 = (a ** 2 + b ** 2) ** 0.5
            r2 = (c ** 2 + d ** 2) ** 0.5
            tr_r1.set(str(round((a ** 2 + b ** 2) ** 0.5, ndigits=common_round)))
            tr_r2.set(str(round((c ** 2 + d ** 2) ** 0.5, ndigits=common_round)))

            quarter1 = get_quarter(a, b)
            quarter2 = get_quarter(c, d)
            fi1 = 0
            fi2 = 0
            match quarter1:
                case 1:
                    fi1 = math.atan(b / a)
                case 4:
                    fi1 = math.atan(b / a)
                case 2:
                    fi1 = math.atan(b / a) + math.pi
                case 3:
                    fi1 = math.atan(b/a) - math.pi
            f1.set(f'{round(fi1, ndigits=common_round)}; {quarter1} четверть')
            match quarter2:
                case 1:
                    fi2 = math.atan(d / c)
                case 4:
                    fi2 = math.atan(d / c)
                case 2:
                    fi2 = math.atan(d / c) + math.pi
                case 3:
                    fi2 = math.atan(d / c) - math.pi
            f2.set(f'{round(fi2, ndigits=common_round)}; {quarter2} четверть')

            tr_mult.set(f'{round(r1 * r2, ndigits=common_round)} * e ^ (i * {round(fi1 + fi2, ndigits=common_round)})')
            tr_div.set(f'{round(r1 / r2, ndigits=common_round)} * e ^ (i * {round(fi1 - fi2, ndigits=common_round)})')

            tr_deg1.set(f'{round(r1 ** common_n * math.cos(common_n * fi1), ndigits=common_round)} + i * '
                        f'{round(r1 ** common_n * math.sin(common_n * fi1), ndigits=common_round)}')
            tr_deg2.set(f'{round(r2 ** common_n * math.cos(common_n * fi2), ndigits=common_round)} + i * '
                        f'{round(r2 ** common_n * math.sin(common_n * fi2), ndigits=common_round)}')

        except (ValueError, ZeroDivisionError, NameError, SyntaxError):
            test_input.set('Данные комплексные числа не поддаются логике')
            sum_z.set(common_error)
            diff_z.set(common_error)
            mult.set(common_error)
            div.set(common_error)
            tr_r1.set(common_error)
            tr_r2.set(common_error)
            f1.set(common_error)
            f2.set(common_error)
            tr_mult.set(common_error)
            tr_div.set(common_error)
            tr_deg1.set(common_error)
            tr_deg2.set(common_error)


    # -------------------RESULT-------------------
    result = ttk.Button(frame_input, text='=', command=get_result)
    result.grid(row=0, column=4, rowspan=2, sticky=NSEW, padx=20)


def create_window():
    root = Tk()
    root.title('Простейший калькулятор комплексных чисел')
    root.geometry('1000x500+330+150')
    root.attributes('-alpha', 0.9)
    root.resizable(False, False)
    root.config(background='#D2E7F5')

    photo = PhotoImage(file='icon.png')
    root.iconphoto(False, photo)

    fill_the_windows(root)

    root.mainloop()


if __name__ == "__main__":
    create_window()