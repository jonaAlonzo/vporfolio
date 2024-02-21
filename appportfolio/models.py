# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

################################################
#  - Empresa
################################################

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    direccion = models.TextField()
    correo_electronico = models.EmailField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Empresas"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

  

################################################
#  - habilidades
################################################


class Habilidad(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    class Meta:
        verbose_name = 'Habilidad' #puede ser otro nombre
        verbose_name_plural = 'Habilidades' # corrected the attribute name
        ordering = ['nombre']

    def __str__(self):
        return "%s,%s" % (self.nombre, self.descripcion)



################################################
# 1 - Categoria
################################################
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField('Puesto de Trabajo',max_length=30,null=True, blank=True)

    class Meta:
        verbose_name = 'Categoria' #puede ser otro nombre
        verbose_name_plural = 'Categorias'
        ordering = ['nombre_categoria']

    def __str__(self):
        return "%s,%s % (self.id,self.nombre_categoria)"

################################################
# 2 - Experiencias
################################################
class Experiencia(models.Model):
    id = models.AutoField(primary_key=True)
    empresa = models.CharField('Empresa',max_length=50,null=True, blank=True)
    fecha_inicio= models.DateField('Fecha de Inicio',null=True, blank=True)
    fecha_fin = models.DateField('Fecha de Finalización', null=True, blank=True)
    observaciones = models.CharField('Funciones', max_length=50, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, related_name='expe_categoria', null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Experiencia' #puede ser otro nombre
        verbose_name_plural = 'Experiencias'
        ordering = ['empresa']

    def __str__(self):
        return "%s,%s,%s,%s,%s,%s % (self.id,self.empresa.self.fecha_inicio,self.fecha_fin,self.observaciones,self.categoria)"

################################################
# Estudios
################################################

class Estudio(models.Model):
    id = models.AutoField(primary_key=True)
    nivelEstudio = models.CharField(max_length=50)
    fecha_inicio = models.DateField(auto_now=True)
    fecha_fin = models.DateField(auto_now=True)
    nota_media = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Estudio'
        verbose_name_plural = 'Estudios'
        ordering = ['id', 'fecha_inicio', 'fecha_fin', 'nota_media' , 'nivelEstudio']

    def __str__(self):
        return f"{self.id} - {self.nivelEstudio} ({self.fecha_inicio} to {self.fecha_fin}) - Nota Media: {self.nota_media}"
    
    
    
################################################
# Seguidor
################################################
class Seguidor(models.Model):
    id = models.AutoField(primary_key=True)
    seguidor = models.CharField('Seguidor',max_length=50,null=True, blank=True)
    

    class Meta:
        verbose_name = 'Seguidor' #puede ser otro nombre
        verbose_name_plural = 'seguidores'
        ordering = ['seguidor']

    def __str__(self):
        return "%s,%s,%s,%s,%s,%s % (self.id,self.self.seguidor)"
        
        
        
################################################
# Seguido
################################################
class Seguido(models.Model):
    id = models.AutoField(primary_key=True)
    seguido = models.CharField('Seguido',max_length=50,null=True, blank=True)
    

    class Meta:
        verbose_name = 'Seguido' #puede ser otro nombre
        verbose_name_plural = 'seguidos'
        ordering = ['seguido']

    def __str__(self):
        return "%s,%s,%s,%s,%s,%s % (self.id,self.self.seguidor)"
        
        
################################################
# Notificacion
################################################
class Notificacion(models.Model):
    id=models.AutoField(primary_key=True)
    Notificacion=models.ForeignKey('self',related_name='notificacion',null=True,blank=True,on_delete=models.PROTECT)
    fecha=models.DateField()
    
    class Meta:
        verbose_name = 'Notificacion'
        verbose_name_plural = 'Notificaciones'
        ordering = ['id','Notificacion','fecha']    
    def __str__(self):
            return f"{self.id} - {self.Notificacion} - {self.fecha}"