from graphics import *
import random
from PIL import Image


class KandinskyBot:
	def __init__(self, width=600, height=400, max_polygons=4, max_lines=7, max_circles=5, max_triangles=4):
		self.width = width
		self.height = height
		self.max_polygons = max_polygons
		self.max_lines = max_lines
		self.max_circles = max_circles
		self.max_triangles = max_triangles

	def paint(self):
		self.start_new_window()
		self.draw_background()
		self.draw_polygons()
		self.draw_lines()
		self.draw_circles()
		self.draw_triangles()

	def draw_background(self):
		background = Rectangle(Point(0,0), Point(self.width, self.height))
		self.draw_and_color(background)

	def draw_polygons(self):
		for _ in range(random.randint(0, self.max_polygons)):
			self.draw_polygon(random.randint(4,7))

	def draw_lines(self):
		for _ in range(random.randint(0, self.max_lines)):
			self.draw_line()

	def draw_circles(self):
		for _ in range(random.randint(0, self.max_circles)):
			self.draw_circle()

	def draw_triangles(self):
		for _ in range(random.randint(0, self.max_triangles)):
			self.draw_polygon(3, color_prob=0.7)

	def draw_polygon(self, n_sides, color_prob=0.3):
		vertices = self.get_random_point_set(n_sides)
		polygon = Polygon(vertices)
		self.draw_and_color(polygon, color_prob=color_prob)

	def draw_line(self):
		endpoints = self.get_random_point_set(2)
		line = Line(*endpoints)
		self.draw(line)

	def draw_circle(self, max_size=100, color_prob=0.6):
		center = self.get_random_point()
		radius = random.randint(0, max_size)
		circle = Circle(center, radius)
		self.draw_and_color(circle, color_prob=color_prob)

	def draw_and_color(self, shape, color_prob=1):
		self.randomly_color(shape, color_prob=color_prob)
		self.draw(shape)

	def draw(self, shape):
		shape.draw(self.window)

	def randomly_color(self, shape, color_prob=1):
		if random.random() < color_prob:
			shape.setFill(self.get_random_color())

	def get_random_point_set(self, n_points):
		return [self.get_random_point() for _ in range(n_points)]

	def get_random_point(self):
		return Point(random.randint(0, self.width), random.randint(0, self.height))

	def get_random_color(self):
		return color_rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255))

	def start_new_window(self):
		self.window = GraphWin('canvas', self.width, self.height)

	def save_image(self, file_name, location='images'):
		self.window.postscript(file='{}/{}.eps'.format(location, file_name), colormode='color')
		self.close_window()
		img = Image.open('{}/{}.eps'.format(location, file_name))
		img.close()

	def close_window(self):
		self.window.close()