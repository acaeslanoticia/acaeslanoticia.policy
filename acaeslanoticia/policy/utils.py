# -*- coding: utf-8 -*-

from plone.i18n.normalizer import idnormalizer
import logging

logger = logging.getLogger('canaimagnulinux.web.policy')


def _add_id(structure):
    """ Add a key for the id as the normalized title, if it does not exists. """
    for item in structure:
        item.setdefault('id', idnormalizer.normalize(item['title'], 'es'))
        if '_children' in item:
            item['_children'] = _add_id(item['_children'])
    return structure
