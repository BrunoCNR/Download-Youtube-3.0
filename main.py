import tkinter as tk
from tkinter import *
from pytube import YouTube, Playlist
from tkinter import filedialog, messagebox

tela = tk.Tk()
tela.geometry('1003x553')
tela.title('Opções de Download')
bg = PhotoImage(file="youtubes.png", width=1000, height=550)
label1 = Label(tela, image=bg)
label1.place(x=0, y=0)


tela.iconphoto(False, PhotoImage(file='ico.png'))
list_box = Listbox(tela, width=90, height=25, bg='black', foreground='white')


sbr = Scrollbar(list_box)
sbr.pack(side=RIGHT, fill="y")
list_box.pack(side=LEFT, fill='both', expand=True)

sbr.config(command=list_box.yview)
list_box.config(yscrollcommand=sbr.set)

list_box.place(relx=0.55, rely=0.300, relheight=0.58, relwidth=0.37)
# JANELA UM


def download():
    url = videodown.get()
    folder = locadal_path.get()
    get_video = YouTube(url)
    get_stream = get_video.streams.get_highest_resolution()
    get_stream.download(folder)
    list_box.insert(0, 'Finalizado :'+get_video.title)
    messagebox.showinfo('Download Youtube', 'Download Finalizado \n' + folder)


def browse():
    download_dir = filedialog.askdirectory(initialdir="C:/Users/Bruno/Music")
    locadal_path.set(download_dir)


def janela_unico():
    janela_download = tk.Toplevel()
    janela_download.title('Download Unico')
    janela_download.config(bg='firebrick3')
    janela_download.iconphoto(False, PhotoImage(file='ico.png'))
    # textos
    label_nome1 = tk.Label(janela_download, text='Local de download:', bg='firebrick3', foreground='white')
    label_nome1.grid(row=1, column=1)

    link_label2 = tk.Label(janela_download, text="YouTube Link :", pady=5, padx=5, bg='firebrick3', foreground='white')
    link_label2.grid(row=2, column=1)
    # labels
    janela_download.Label_text = Entry(janela_download, width=60, textvariable=locadal_path)
    janela_download.Label_text.grid(row=1, column=2)

    tela.link_text = Entry(janela_download, width=60, textvariable=videodown)
    tela.link_text.grid(row=2, column=2)
    # botoes
    botao_procura = Button(janela_download, text='Procurar', command=browse, width=10, bg='lightblue')
    botao_procura.grid(row=1, column=3)

    botao_download = Button(janela_download, text='Baixar Video', command=download, width=25, bg='lightblue')
    botao_download.grid(row=3, column=2)


# JANELA 3


def janela_tres():
    janela_download = tk.Toplevel()
    janela_download.config(bg='firebrick3')
    janela_download.title('Download PlayList')
    janela_download.iconphoto(False, PhotoImage(file='ico.png'))
    # textos
    label_nome1 = tk.Label(janela_download, text='Local de download:', bg='firebrick3', foreground='white')
    label_nome1.grid(row=1, column=1)

    link_label2 = tk.Label(janela_download, text="YouTube PlayList :", pady=5, padx=5, bg='firebrick3',
                           foreground='white')
    link_label2.grid(row=2, column=1)
    # labels
    janela_download.Label_text = Entry(janela_download, width=60, textvariable=locadal_path)
    janela_download.Label_text.grid(row=1, column=2)

    tela.link_text = Entry(janela_download, width=60, textvariable=videodown)
    tela.link_text.grid(row=2, column=2)
    # botoes
    botao_procura = Button(janela_download, text='Procurar', command=browse2, width=10, bg='lightblue')
    botao_procura.grid(row=1, column=3)

    botao_download = Button(janela_download, text='Baixar Videos', command=download2, width=25, bg='lightblue')
    botao_download.grid(row=3, column=2)


def browse2():
    downloads_dir = filedialog.askdirectory(initialdir="C:/Users/Bruno/Music")
    locadal_path.set(downloads_dir)


def download2():
    url = videodown.get()
    folder = locadal_path.get()
    get_video = Playlist(url)
    for video in get_video.videos:
        video.streams.get_highest_resolution().download(folder)
        list_box.insert(0, 'Finalizado :' + video.title)
    messagebox.showinfo('Download Youtube', 'Downloads Finalizados \n' + folder)

# JANELA 4


def janela_quatro():
    janela_download = tk.Toplevel()
    janela_download.title('Download PlayList')
    janela_download.config(bg='firebrick3')
    janela_download.iconphoto(False, PhotoImage(file='ico.png'))
    # textos
    label_nome1 = tk.Label(janela_download, text='Local de download:', bg='firebrick3', foreground='white')
    label_nome1.grid(row=1, column=1)

    link_label2 = tk.Label(janela_download, text="YouTube Audio MP4 :", pady=5, padx=5, bg='firebrick3',
                           foreground='white')
    link_label2.grid(row=2, column=1)
    # labels
    janela_download.Label_text = Entry(janela_download, width=60, textvariable=locadal_path)
    janela_download.Label_text.grid(row=1, column=2)

    tela.link_text = Entry(janela_download, width=60, textvariable=videodown)
    tela.link_text.grid(row=2, column=2)

    # botoes
    botao_procura = Button(janela_download, text='Procurar', command=browse4, width=10, bg='lightblue')
    botao_procura.grid(row=1, column=3)

    botao_download = Button(janela_download, text='Baixar Audio', command=download4, width=25, bg='lightblue')
    botao_download.grid(row=3, column=2)


def browse4():
    downloads_dir = filedialog.askdirectory(initialdir="C:/Users/Bruno/Music")
    locadal_path.set(downloads_dir)


def download4():
    url = videodown.get()
    folder = locadal_path.get()
    audio = YouTube(url)
    mp4 = audio.streams.get_audio_only()
    mp4.download(folder)
    list_box.insert(0, 'Finalizado :' + audio.title)
    messagebox.showinfo('Download Audio .MP4 Youtube', 'Downloads Finalizados \n' + folder)

# janela 5


def janela_cinco():
    janela_download = tk.Toplevel()
    janela_download.title('Download PlayList')
    janela_download.config(bg='firebrick3')
    janela_download.iconphoto(False, PhotoImage(file='ico.png'))
    # textos
    label_nome1 = tk.Label(janela_download, text='Local de download:', bg='firebrick3', foreground='white')
    label_nome1.grid(row=1, column=1)

    link_label2 = tk.Label(janela_download, text="YouTube PlayList Audio MP4 :", pady=5, padx=5, bg='firebrick3',
                           foreground='white')
    link_label2.grid(row=2, column=1)
    # labels
    janela_download.Label_text = Entry(janela_download, width=60, textvariable=locadal_path)
    janela_download.Label_text.grid(row=1, column=2)

    tela.link_text = Entry(janela_download, width=60, textvariable=videodown)
    tela.link_text.grid(row=2, column=2)

    # botoes
    botao_procura = Button(janela_download, text='Procurar', command=browse5, width=10, bg='lightblue')
    botao_procura.grid(row=1, column=3)

    botao_download = Button(janela_download, text='Baixar PlayList Audio', command=download5, width=25, bg='lightblue')
    botao_download.grid(row=3, column=2)


def browse5():
    downloads_dir = filedialog.askdirectory(initialdir="C:/Users/Bruno/Music")
    locadal_path.set(downloads_dir)


def download5():
    url = videodown.get()
    folder = locadal_path.get()
    audio = Playlist(url)
    for video in audio.videos:
        video.streams.get_audio_only().download(folder)
        list_box.insert(0, 'Finalizado :' + video.title)
    messagebox.showinfo('Download Audio .MP4 Youtube', 'Downloads Finalizados \n'+folder)


locadal_path = StringVar()
videodown = StringVar()


# TELA 1

botao = Button(tela, width=25, text='Download video único', command=janela_unico, relief='sunken', bg='firebrick3',
               foreground='white',
               font='Arial 10')
botao.place(relx=0.1, rely=0.09, relheight=0.05, relwidth=0.3)

botao = Button(tela, width=25, text='Download de PlayList', command=janela_tres, relief='sunken', bg='firebrick3',
               foreground='white',
               font='Arial 10')
botao.place(relx=0.1, rely=0.15, relheight=0.05, relwidth=0.3)

botao = Button(tela, width=25, text='Download de audio único', command=janela_quatro, relief='sunken', bg='firebrick3',
               foreground='white',
               font='Arial 10')
botao.place(relx=0.1, rely=0.21, relheight=0.05, relwidth=0.3)

botao = Button(tela, width=25, text='Download de audio de PlayList', command=janela_cinco, relief='sunken',
               foreground='white',
               bg='firebrick3', font='Arial 10')
botao.place(relx=0.1, rely=0.27, relheight=0.05, relwidth=0.3)

Label(tela, width=50, text='--~~> Bruno L <~~--', background='black', foreground='white', font='Arial 10')\
    .place(relx=0.59, rely=0.943, relheight=0.05, relwidth=0.3)

tela.mainloop()
