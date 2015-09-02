.. -*- coding: utf-8 -*-

.. contents:: Tabla de Contenidos

Introducción
============

Este producto Policy de Plone ofrece varios perfiles de instalación para el sitio ACA es la Noticia (Agencia Comunicacional Alternativa).

Características
===============

Este producto habilita las siguientes configuraciones:

- TODO.

Instalación
===========

Este proyecto debe ser instalado usando configuraciones buildout. Debe leer el archivo
``INSTALL.txt`` en la carpeta ``docs`` de este producto.


Insignias de calidad
--------------------

.. image:: https://d2weczhvl823v0.cloudfront.net/acaeslanoticia/acaeslanoticia.policy/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

.. image:: https://travis-ci.org/acaeslanoticia/acaeslanoticia.policy.svg?branch=master
   :target: https://travis-ci.org/acaeslanoticia/acaeslanoticia.policy

.. image:: https://coveralls.io/repos/acaeslanoticia/acaeslanoticia.policy/badge.png
   :target: https://coveralls.io/r/acaeslanoticia/acaeslanoticia.policy

Dependencias del sitio
----------------------

Dependencias usadas en el sitio de Canaima GNU/Linux.

.. list-table:: Dependencias extras
   :widths: 10 10 10 10
   :header-rows: 1

   * - Nombre de paquete
     - Versión
     - Pruebas
     - Pruebas de cobertura
   * - Products.Doormat
     - |Products.Doormat.v|
     - |Products.Doormat.t|
     - |Products.Doormat.c|
   * - brasil.gov.tiles
     - |brasil.gov.tiles.v|
     - |brasil.gov.tiles.t|
     - |brasil.gov.tiles.c|
     - |brasil.gov.tiles.v|
   * - acaeslanoticia.theme
     - |acaeslanoticia.theme.t|
     - |acaeslanoticia.theme.c|
   * - collective.disqus
     - |collective.disqus.v|
     - |collective.disqus.t|
     - |collective.disqus.c|
   * - collective.googlenews
     - |collective.googlenews.v|
     - |collective.googlenews.t|
     - |collective.googlenews.c|
   * - collective.nitf
     - |collective.nitf.v|
     - |collective.nitf.t|
     - |collective.nitf.c|
   * - collective.opendata
     - |collective.opendata.v|
     - |collective.opendata.t|
     - |collective.opendata.c|
   * - collective.polls
     - |collective.polls.v|
     - |collective.polls.t|
     - |collective.polls.c|
   * - collective.upload
     - |collective.upload.v|
     - |collective.upload.t|
     - |collective.upload.c|
   * - ftw.avatar
     - |ftw.avatar.v|
     - |ftw.avatar.t|
     - |ftw.avatar.c|
   * - plone.api
     - |plone.api.v|
     - |plone.api.t|
     - |plone.api.c|
   * - sc.social.like
     - |sc.social.like.v|
     - |sc.social.like.t|
     - |sc.social.like.c|

Pruebas
=======

Para ejecutar las pruebas del paquete debe ubicarse en el directorio de su proyecto 
Buildout, y ejecutar en una consola de comando el siguiente comando:

::

    $ ./bin/test -s acaeslanoticia.policy

Si necesita saber cual son las pruebas disponibles para este producto ejecute el 
siguiente comando:

::

    $ ./bin/test -s acaeslanoticia.policy --list-tests

Para correr una prueba en especifica coloque el parámetro ``-t`` y el nombre de 
la función correspondiente, a continuación un ejemplo con el siguiente comando:

::

    $ ./bin/test -s acaeslanoticia.policy -t test_portal_title

Para ver más opciones para ejecutar sus pruebas ejecute el siguiente comando:

::

    $ ./bin/test --help


Soporte
=======

¿Tienes una idea?, ¿Encontraste un error? Háganos saber mediante la `apertura de un ticket de soporte`_.


Autor(es) Original(es)
======================

* Leonardo J .Caballero G. aka macagua

Colaboraciones impresionantes
=============================

* Nombre Completo aka apodo

Par una lista actualizada de todo los colaboradores visite: https://github.com/canaimagnulinux/acaeslanoticia.policy/contributors

.. _apertura de un ticket de soporte: https://github.com/acaeslanoticia/acaeslanoticia.policy/issues

.. |Products.Doormat.v| image:: http://img.shields.io/pypi/v/Products.Doormat.svg
   :target: https://pypi.python.org/pypi/Products.Doormat
.. |Products.Doormat.t| image:: https://secure.travis-ci.org/collective/Products.Doormat.png
   :target: http://travis-ci.org/collective/Products.Doormat
.. |Products.Doormat.c| image:: https://coveralls.io/repos/collective/Products.Doormat/badge.png?branch=master
   :target: https://coveralls.io/r/collective/Products.Doormat

.. |brasil.gov.tiles.v| image:: http://img.shields.io/pypi/v/brasil.gov.tiles.svg
   :target: https://pypi.python.org/pypi/brasil.gov.tiles
.. |brasil.gov.tiles.t| image:: https://secure.travis-ci.org/plonegovbr/brasil.gov.tiles.png
   :target: http://travis-ci.org/plonegovbr/brasil.gov.tiles
.. |brasil.gov.tiles.c| image:: https://coveralls.io/repos/plonegovbr/brasil.gov.tiles/badge.png?branch=master
   :target: https://coveralls.io/r/plonegovbr/brasil.gov.tiles

.. |collective.polls.v| image:: http://img.shields.io/pypi/v/collective.polls.svg
   :target: https://pypi.python.org/pypi/collective.polls
.. |collective.polls.t| image:: https://secure.travis-ci.org/collective/collective.polls.png
   :target: http://travis-ci.org/collective/collective.polls
.. |collective.polls.c| image:: https://coveralls.io/repos/collective/collective.polls/badge.png?branch=master
   :target: https://coveralls.io/r/collective/collective.polls

.. |acaeslanoticia.theme.v| image:: http://img.shields.io/pypi/v/acaeslanoticia.theme.svg
   :target: https://pypi.python.org/pypi/acaeslanoticia.theme
.. |acaeslanoticia.theme.t| image:: https://secure.travis-ci.org/acaeslanoticia/acaeslanoticia.theme.png
   :target: http://travis-ci.org/acaeslanoticia/acaeslanoticia.theme
.. |acaeslanoticia.theme.c| image:: https://coveralls.io/repos/acaeslanoticia/acaeslanoticia.theme/badge.png?branch=master
   :target: https://coveralls.io/r/acaeslanoticia/canaimagnulinux.web.theme

.. |collective.cover.v| image:: http://img.shields.io/pypi/v/collective.cover.svg
   :target: https://pypi.python.org/pypi/collective.cover
.. |collective.cover.t| image:: https://secure.travis-ci.org/collective/collective.cover.png
   :target: http://travis-ci.org/collective/collective.cover
.. |collective.cover.c| image:: https://coveralls.io/repos/collective/collective.cover/badge.png?branch=master
   :target: https://coveralls.io/r/collective/collective.cover

.. |collective.disqus.v| image:: http://img.shields.io/pypi/v/collective.disqus.svg
   :target: https://pypi.python.org/pypi/collective.disqus
.. |collective.disqus.t| image:: https://secure.travis-ci.org/collective/collective.disqus.png
   :target: http://travis-ci.org/collective/collective.disqus
.. |collective.disqus.c| image:: https://coveralls.io/repos/collective/collective.disqus/badge.png?branch=master
   :target: https://coveralls.io/r/collective/collective.disqus

.. |collective.googlenews.v| image:: http://img.shields.io/pypi/v/collective.googlenews.svg
   :target: https://pypi.python.org/pypi/collective.googlenews
.. |collective.googlenews.t| image:: https://secure.travis-ci.org/collective/collective.googlenews.png
   :target: http://travis-ci.org/collective/collective.googlenews
.. |collective.googlenews.c| image:: https://coveralls.io/repos/collective/collective.googlenews/badge.png?branch=master
   :target: https://coveralls.io/r/collective/collective.googlenews

.. |collective.nitf.v| image:: http://img.shields.io/pypi/v/collective.nitf.svg
   :target: https://pypi.python.org/pypi/collective.nitf
.. |collective.nitf.t| image:: https://secure.travis-ci.org/collective/collective.nitf.png
   :target: http://travis-ci.org/collective/collective.nitf
.. |collective.nitf.c| image:: https://coveralls.io/repos/collective/collective.nitf/badge.png?branch=master
   :target: https://coveralls.io/r/collective/collective.nitf

.. |collective.opendata.v| image:: http://img.shields.io/pypi/v/collective.opendata.svg
   :target: https://pypi.python.org/pypi/collective.opendata
.. |collective.opendata.t| image:: https://secure.travis-ci.org/plonegovbr/collective.opendata.png
   :target: http://travis-ci.org/collective/collective.opendata
.. |collective.opendata.c| image:: https://coveralls.io/repos/plonegovbr/collective.opendata/badge.png?branch=master
   :target: https://coveralls.io/r/collective/collective.opendata

.. |collective.upload.v| image:: http://img.shields.io/pypi/v/collective.upload.svg
   :target: https://pypi.python.org/pypi/collective.upload
.. |collective.upload.t| image:: https://secure.travis-ci.org/collective/collective.upload.png
   :target: http://travis-ci.org/collective/collective.upload
.. |collective.upload.c| image:: https://coveralls.io/repos/collective/collective.upload/badge.png?branch=master
   :target: https://coveralls.io/r/collective/collective.upload

.. |ftw.avatar.v| image:: http://img.shields.io/pypi/v/ftw.avatar.svg
   :target: https://pypi.python.org/pypi/ftw.avatar
.. |ftw.avatar.t| image:: https://secure.travis-ci.org/4teamwork/ftw.avatar.png
   :target: http://travis-ci.org/4teamwork/ftw.avatar
.. |ftw.avatar.c| image:: https://coveralls.io/repos/4teamwork/ftw.avatar/badge.png?branch=master
   :target: https://coveralls.io/r/4teamwork/ftw.avatar

.. |plone.api.v| image:: http://img.shields.io/pypi/v/plone.api.svg
   :target: https://pypi.python.org/pypi/plone.api
.. |plone.api.t| image:: https://secure.travis-ci.org/plone/plone.api.png
   :target: http://travis-ci.org/collective/plone.api
.. |plone.api.c| image:: https://coveralls.io/repos/plone/plone.api/badge.png?branch=master
   :target: https://coveralls.io/r/collective/plone.api

.. |sc.social.like.v| image:: http://img.shields.io/pypi/v/sc.social.like.svg
   :target: https://pypi.python.org/pypi/sc.social.like
.. |sc.social.like.t| image:: https://secure.travis-ci.org/collective/sc.social.like.png
   :target: http://travis-ci.org/collective/sc.social.like
.. |sc.social.like.c| image:: https://coveralls.io/repos/collective/sc.social.like/badge.png?branch=master
   :target: https://coveralls.io/r/collective/sc.social.like

