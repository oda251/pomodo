import datetime
import time
import os
import flet as ft

def main(page: ft.Page):
	current_time = 0
	ct_text = "{:02}:{:02}".format(current_time % 3600 // 60, current_time % 60)
	clock = ft.Text(
		str(ct_text),
		size=80,
		style=ft.FontWeight.BOLD
		)
	component = ft.Container(
		content=clock,
		alignment=ft.alignment.center,
		width=500,
		height=500,
	)
	page.add(component)
	os.system("osascript -e 'display notification \"ぽもだよ\" with title \"ポモドーロタイマー\" sound name \"Glass\"'")
	flag = 0
	while True:
		time.sleep(1)
		current_time += 1
		if flag == 0 and current_time == 25 * 60:
			os.system("osascript -e 'display notification \"25ふんたったよ\" with title \"ポモドーロタイマー\" sound name \"Glass\"'")
			current_time = 0
			flag = 1
		elif flag == 1 and current_time == 5 * 60:
			os.system("osascript -e 'display notification \"5ふんたったよ\" with title \"ポモドーロタイマー\" sound name \"Glass\"'")
			current_time = 0
			flag = 0
		ct_text = "{:02}:{:02}".format(current_time % 3600 // 60, current_time % 60)
		clock.value = ct_text
		page.update()

if __name__ == "__main__":
	ft.app(target = main)