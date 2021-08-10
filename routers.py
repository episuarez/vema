from vema import Page

def load_routers(app):
	@app.route('/pages/example')
	def example():
		return Page('pages/example.md').render()

	@app.route('/')
	def index():
		return Page('pages/index.html').render()

