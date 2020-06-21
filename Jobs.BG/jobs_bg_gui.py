import tkinter as tk
from jobsbg.job import Job
from jobsbg.jobs_bg_scraper import JobsScraper


class JobsbgGUI:
    def __init__(self):
        self.root = tk.Tk()

    def run(self):
        self.root.geometry('1100x500+50+50')
        self.root.resizable(0, 0)
        self.root.title('Jobs.bg Scraper')

        w = tk.Label(self.root, text="Jobs.BG Scraper", font='Times 32 bold', fg='black', pady=20).pack()

        def on_click(event):
            event.widget.pack_forget()
            self.getJobs()

        button = tk.Button(self.root, text='Scrap jobs!', background='violet',
                           width=20, height=3, font='Times 24 bold')
        button.bind('<Button-1>', on_click)
        button.pack(anchor='center')

        self.root.mainloop()

    def loadJobs(self, jobs):
        canvas = tk.Canvas(self.root, borderwidth=0,
                           width=1000, height=600)
        frame = tk.Frame(canvas)
        vsb = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)

        vsb.pack(side="right", fill="y")
        canvas.pack(pady=30, expand=True)
        canvas.create_window((20, 20), window=frame, anchor='nw')

        frame.bind("<Configure>", lambda event,
                                         canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind('<Enter>', lambda _: canvas.bind_all("<MouseWheel>", _on_mousewheel))
        canvas.bind('<Leave>', lambda _: canvas.unbind_all("<MouseWheel>"))

        idx = 1
        for job in jobs:
            t = str(idx) + ': ' + str(job)
            tk.Label(frame, text=t, width=116, height=2,
                     borderwidth='2', relief='solid', font='Times 12 bold').grid(row=idx, column=1)
            idx += 1

    def getJobs(self):
        jobsbg = JobsScraper()
        jobsbg.click_it_category()
        jobsbg.write_search_town_salary(only_salary=True)
        jobsbg.search()

        jobs = jobsbg.explore_pages()
        jobsbg.quit()

        self.loadJobs(jobs)