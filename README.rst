=================
 Visual Title
=================

.. contents:: :local:

Introduction
-------------

This add-on separates navigation title and visual title fields in Plone.
This serves the needs of marketing message where

* The author wants long, marketing pitch tuned, title for the page

* For the navigation tree, shorter, informative title is preferred

The add-on is also useful for languages preferring long words, like German and Finnish,
where the actual title does not fit well into the navigation tree and
a shortened title may be preferred.

Not Entirely Unlike
+++++++++++++++++++
`collective.navigationtitle <https://github.com/collective/collective.navigationtitle>`_ - provides a dexterity behaviour that does a similar job for dexterity types.

Compatibility
----------------

Plone 4+

Installation
-------------

Add ``visualtitle`` in buildout.cfg::

    [buildout]

    eggs =
        ...
        visualtitle


Install the add-on using the add-on installer in Site Setup.

.. note ::

    For Plone 4.1 or lower: Add Dexterity extends = line in buildout.cfg


* http://plone.org/products/dexterity/documentation/how-to/install

Usage
------

The add-on currently supports `Archetypes <http://collective-docs.readthedocs.org/en/latest/content/archetypes/index.html>`_ based content.

When the add-on is activated you see title and visual title fields on Archetypes edit pages
on all Archetypes content pages.

Limitations
-------------

The page template must use Plone 4+ ``content-core`` slots or ``generic_title_view`` macro to render the page title.

Correct example 1::

    <html xmlns="http://www.w3.org/1999/xhtml"
          xmlns:metal="http://xml.zope.org/namespaces/metal"
          xmlns:tal="http://xml.zope.org/namespaces/tal"
          xmlns:i18n="http://xml.zope.org/namespaces/i18n"
          metal:use-macro="context/main_template/macros/master">

        <metal:block fill-slot="content-core">
            .. page payload goes here ...
        </metal:block>
    </html>

Correct example 2::

    <h1 metal:use-macro="context/kss_generic_macros/macros/generic_title_view">
         Generic KSS Title. Is rendered with class="documentFirstHeading".
    </h1>

If you do like this for your own content types the visual title magic won't take a place::

    <h1 class="documentFirstHeading">My title</h1>

You can also access the visual title directly (not recommended)::

    <h1 tal:content="python:context.restrictedTraverse('visualtitle')()" class="documentFirstHeading" />

Internals
-----------

This add-on overrides ``kss_generic_macros`` template for Plone 4+,
adds new fields using archetypes.schemaextender and a helper view
which you can call from the code to get the visual title.

i18n
-----

Yep, it does.

Source and issue tracking
---------------------------

* https://github.com/miohtama/visualtitle

Policy and source coding conventions
+++++++++++++++++++++++++++++++++++++

The code follows Pylint policies defined in `VVV policy file <http://pypi.python.org/pypi/vvv>`_.

The code is PEP-8 compatible for the parts where PEP-8 does not get confused.

Author
--------

`Mikko Ohtamaa <http://opensourcehacker.com>`_

