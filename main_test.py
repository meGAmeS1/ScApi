import json
import settings
import logging
from client import SensCritiqueClient
from models import Universe, SubUniverse, SearchFilter

logger = logging.getLogger(__name__)


# A little function to pretty print JSON
def pp_json(data):
    print json.dumps(data, indent=4, sort_keys=True)


client = SensCritiqueClient()
client.login(settings.LOGIN, settings.PASSWORD)

# wishes = client.l_get_wishes_all(Universe.Music)
# logger.info("Id = {id}".format(id=wishes[0].id))
# logger.info("Title = {title}".format(title=wishes[0].title))
# logger.info("Trailer = {title}".format(title=wishes[0].trailers))
#
# logger.info("User = {user}".format(user=client.l_get_userinfo().displayed_name))
#
# # Perform a search request
# logger.info("Searching for \"fiesta\" games...")
# found_products = client.search('fiesta', filter=SearchFilter.GAMES_ONLY)
#
# logger.info("Found [{nb_games}] games".format(nb_games=len(found_products)))
#
# for game in found_products:
#     logger.info("  - {title}".format(title=unicode(game.title).encode('utf8')))
#     logger.info("     * Id = {id}".format(id=game.id))
#     logger.info("     * Rating = {rating}".format(rating=game.rating))
#
# # Add Game Of Thrones in the list
# logger.info("Saving product={productId} into list={listId}".format(productId="225391", listId="1418781"))
# client.save_product_in_list(list_id=1418781, product_id=225391)
#
# # Add a music in a TV Show list (NOT ALLOWED IN THE WEB INTERFACE)
# # Lady In Gold (21196742)
# logger.info("Saving product={productId} into list={listId}".format(productId="21196742", listId="1418781"))
# client.save_product_in_list(list_id=1418781, product_id=21196742)
#
# # Rate Game Of Thrones at 10
# logger.info("Rating GameofThrones with 20...")
# success_rating = client.rate_product(product_id=225391, rating=10);
# logger.info("success_rating = {success_rating}".format(success_rating=success_rating))


# Create a temp list
logger.info("Creating list for subUniverse={sub_universe} for user=me...".format(sub_universe=SubUniverse.Games))
created_list = client.create_list(name="Coucou SC", sub_universe=SubUniverse.Games)
if (not created_list) or (created_list is None):
    logger.error("Error when creating list")
    exit

logger.info("Created list name={name} and id={id}".format(name=created_list.title, id=created_list.id))

# Add a video game in the list
# 8Bit Fiesta - 17106998
height_bit_fiesta_product_id = 17106998
logger.info("Saving product={productId} into list={listId}...".format(productId=height_bit_fiesta_product_id, listId=created_list.id))
client.save_product_in_list(list_id=created_list.id, product_id=height_bit_fiesta_product_id)

# Get the products of the list and check if the product is in the list
logger.info("Listing list={listId}...".format(listId=created_list.id))
products_of_list = client.get_product_list_of_list(created_list.id, limit=20, offset=0)

is_product_in_list = False
for product in products_of_list:
    if product.id == height_bit_fiesta_product_id:
        is_product_in_list = True
        break

if is_product_in_list:
    logger.info("8Bit Fiesta has been found in the list! Congratulation!")
else:
    logger.error("Could not find 8Bit fiesta in the list")

logger.info("Removing product={product} in list...".format(product=height_bit_fiesta_product_id))
is_product_removed = client.remove_product_in_list(product_id=height_bit_fiesta_product_id, list_id=created_list.id)

if is_product_removed:
    logger.info("Product={product_id} has been removed from list".format(product_id=height_bit_fiesta_product_id))
else:
    logger.error("Could not remove product={product_id} from list".format(product_id=height_bit_fiesta_product_id))

logger.info("Deleting list={listId}...".format(listId=created_list.id))
status = client.delete_list(created_list.id)
logger.info("Status = {status}".format(status))