from pelican import signals

import logging

logging.Logger(__name__)


def scrub_articles(sender):
    '''
    Given the article generator as well as using 'EXCLUDE_CATEGORIES' in the settings,
    this will remove articles from the generator that are classed as any of the excluded categories.
    '''

    print "%s blong blonginitialized !!" % sender
    excludes = sender.settings.get('EXCLUDE_CATEGORIES')
    if excludes:
        sender.articles = [x for x in sender.articles if x.category not in excludes]


def register():
    signals.article_generator_pretaxonomy.connect(scrub_articles)
