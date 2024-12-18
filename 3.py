    def generate_numbers(self):
        for i in range(1, 11):
            x, y = random.randint(50, 350), random.randint(50, 350)
            circle = self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightblue", outline="black")
            num = self.canvas.create_text(x, y, text=str(i), font=("Arial", 16), fill="black")
            self.numbers[circle] = (i, circle, num)
            self.numbers[num] = (i, circle, num)
            self.canvas.tag_bind(circle, "<Button-1>", lambda e, n=circle: self.click_number(n))
            self.canvas.tag_bind(num, "<Button-1>", lambda e, n=circle: self.click_number(n))
    def click_number(self, item):
        number, circle, num = self.numbers[item]
        if number == self.current:
            self.canvas.delete(circle)
            self.canvas.delete(num)
            self.current += 1
            if self.current > 10:
                self.end_game()
    def update_timer(self):
        if self.running:
            elapsed = time.time() - self.start_time
            self.hud.config(text=f"Время: {elapsed:.2f} с")
            self.timer_id = self.root.after(50, self.update_timer)
