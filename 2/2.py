    def start_game(self):
        self.start_button.pack_forget()
        self.canvas.delete("all")
        self.hud.config(text="Время: 0.00 с")
        self.hud.pack()
        self.running = True
        self.start_time = time.time()
        self.current = 1
        self.numbers = {}
        self.generate_numbers()
        self.update_timer()
