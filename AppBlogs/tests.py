from django.test import TestCase
from django.urls import reverse
from AppBlogs.models import BusquedaFiltrada


class BlogTestCase(TestCase):
    def setUp(self):
        BusquedaFiltrada.objects.create(nombre_libro="Libro1", nombre_autor="Autor1")
        BusquedaFiltrada.objects.create(nombre_libro="Libro2", nombre_autor="Autor2")

    def test_animals_can_speak(self):
        p1 = BusquedaFiltrada.objects.get(nombre_autor="Autor1")
        p2 = BusquedaFiltrada.objects.get(nombre_autor="Autor2")
        self.assertEqual(p1.nombre_libro, "Libro1")
        self.assertEqual(p2.nombre_libro, "Libro2")


class ViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('MiAppInicio'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bienvenidos, en este blog encontraremos todo tipo de libros y si no lo encuentras lo puedes cargar!!")

    def test_past_question(self):
        i = BusquedaFiltrada.objects.create(nombre_libro="Libro1", nombre_autor="Autor1")
        response = self.client.get(reverse('AppCargar'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f"Nombre del libro: {i.nombre_libro}")


