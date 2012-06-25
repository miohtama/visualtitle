Introduction
-------------

This add-on adds separate navigation title and visual title (in page text) fields for Plone.
This is useful for marketing sites where

* The author wants long, selling, title for the page

* The same long title is too long to be displayed in navigation trees

Compatibility
----------------

Plone 4+

Installation
-------------

Plone 4.1 or lower: Add Dexterity ``extends = `` line in buildout.cfg

* http://plone.org/products/dexterity/documentation/how-to/install

Add ``visualtitle`` in buildout.cfg

    [buildout]

    eggs =
        ...
        visualtitle


Install the add-on using the add-on installer in Site Setup.

Usage
------

When the add-on is activated you see title and visual title fields on Archetypes edit pages
on all Archetypes content pages.

.. note ::

    Dexterity support is planned, but looking for the sponsor.

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

If you do like this for your own content types it won't work::

    <h1 class="documentFirstHeading">My title</h1>

You can also access the visual title directly (not recommended)::

    <h1 tal:content="python:context.restrictedTraverse('visualtitle')()" class="documentFirstHeading" />

Internals
-----------

This add-on overrides Title viewlet for Plone 4+

