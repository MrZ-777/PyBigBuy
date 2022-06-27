# -*- coding: utf-8 -*-

"""
Official documentation for Bigbuy API endpoints can be found at: https://api.bigbuy.eu/rest/doc/
"""
import warnings
from typing import Optional, Dict, Any, Union, Iterable, List, cast

import requests
from api_session import APISession

from . import __version__
from .exceptions import raise_for_response

__all__ = ['BigBuy']

Id = Union[int, str]


class BigBuy(APISession):
    def __init__(self, app_key: Optional[str] = None, mode="sandbox"):
        """Instantiates an instance of BigBuy.

        :param app_key: Your applications key
        :param mode: "sandbox" or "production"
        """
        if mode == "sandbox":
            base_url = 'https://api.sandbox.bigbuy.eu/rest'
        else:  # if mode == "production":
            base_url = 'https://api.bigbuy.eu/rest'

        super().__init__(base_url, user_agent=f'pyBigBuy v{__version__}',
                         none_on_404=False,
                         # BigBuy likes returning '200 OK' responses with empty bodies instead of 404s.
                         none_on_empty=True)

        self.app_key = app_key
        self.headers.setdefault('Authorization', f'Bearer {app_key}')

    def __repr__(self):
        return f'<Bigbuy key={self.app_key[:10]}…>'

    def raise_for_response(self, response: requests.Response):
        # Implement upstream's method
        return raise_for_response(response)

    def request_api(self, method: str, path: str, *args, throw: Optional[bool] = None, **kwargs) \
            -> requests.Response:
        """
        Request BigBuy’s API.
        """
        return super().request_api(method,
                                   f'/{path}.json', *args,
                                   # Default throw= to True unless 'False' was explicitly passed
                                   throw=throw is not False,
                                   **kwargs)

    # catalog
    def get_attribute(self, attribute_id: Id, **params):
        """Get a single attribute."""
        return self.get_json_api(f'catalog/attribute/{attribute_id}', params=params)

    def get_attribute_all_languages(self, attribute_id: Id, **params):
        """Get a single attribute."""
        return self.get_json_api(f'catalog/attributealllanguages/{attribute_id}', params=params)

    def get_attribute_group(self, attribute_group_id: Id, **params):
        """Get a single attribute group."""
        return self.get_json_api(f'catalog/attributegroup/{attribute_group_id}', params=params)

    def get_attribute_group_all_languages(self, attribute_group_id: Id, **params):
        """Get a single attribute group."""
        return self.get_json_api(f'catalog/attributegroupalllanguages/{attribute_group_id}', params=params)

    def get_attribute_groups(self, **params):
        """Lists all attribute groups."""
        return self.get_json_api('catalog/attributegroups', params=params)

    def get_attributes(self, **params):
        """Lists all attributes."""
        return self.get_json_api('catalog/attributes', params=params)

    def get_categories(self, **params):
        """Lists all categories."""
        return self.get_json_api('catalog/categories', params=params)

    def get_category(self, category_id: Id, **params):
        """
        Returns the selected category.
        Note this endpoint has been removed on 2022/05/25.
        """
        return self.get_json_api(f'catalog/category/{category_id}', params=params)

    def get_category_all_languages(self, category_id: Id, **params):
        """Returns the selected category."""
        return self.get_json_api(f'catalog/categoryalllanguages/{category_id}', params=params)

    def get_languages(self, **params):
        """Returns all languages"""
        return self.get_json_api('catalog/languages', params=params)

    def get_manufacturer(self, manufacturer_id: Id, **params):
        """Get a single manufacturer."""
        return self.get_json_api(f'catalog/manufacturer/{manufacturer_id}', params=params)

    def get_manufacturers(self, **params):
        """Lists all manufacturers."""
        return self.get_json_api('catalog/manufacturers', params=params)

    def get_product(self, product_id: Id, **params):
        """Get a single product."""
        return self.get_json_api(f'catalog/product/{product_id}', params=params)

    def get_product_categories(self, product_id: Id, **params):
        """Get product categories."""
        return self.get_json_api(f'catalog/productcategories/{product_id}', params=params)

    def get_product_images(self, product_id: Id, **params):
        """Get a single product images."""
        return self.get_json_api(f'catalog/productimages/{product_id}', params=params)

    def get_product_information(self, product_id: Id, **params):
        """Get a single product information."""
        return self.get_json_api(f'catalog/productinformation/{product_id}', params=params)

    def get_product_information_all_languages(self, product_id: Id, **params):
        """Get a single product."""
        return self.get_json_api(f'catalog/productinformationalllanguages/{product_id}', params=params)

    def get_product_information_by_sku(self, sku: str, **params):
        """Get a single product by sku."""
        return self.get_json_api(f'catalog/productinformationbysku/{sku}', params=params)

    def get_products(self, **params):
        """Returns all products."""
        return self.get_json_api('catalog/products', params=params)

    def get_products_categories(self, **params):
        """Returns all products categories."""
        return self.get_json_api('catalog/productscategories', params=params)

    def get_products_images(self, **params):
        """Returns all products images."""
        return self.get_json_api('catalog/productsimages', params=params)

    def get_products_information(self, **params):
        """Returns all products products information."""
        return self.get_json_api('catalog/productsinformation', params=params)

    def get_products_stock(self, **params):
        """Returns all products stock."""
        return self.get_json_api('catalog/productsstock', params=params)

    def get_products_stock_available(self, **params):
        """Returns all products with available stock."""
        return self.get_json_api('catalog/productsstockavailable', params=params)

    def get_products_stock_by_reference(self, skus: Iterable[str]):
        """Get all selected products stock."""
        payload = {
            "product_stock_request": {
                "products": [{"sku": sku} for sku in skus],
            }
        }
        return self.post_api('catalog/productsstockbyreference', json=payload).json()

    def get_products_tags(self, **params):
        """Lists all product tags."""
        return self.get_json_api('catalog/productstags', params=params)

    def get_product_stock(self, product_id: Id, **params):
        """Get a single product stock."""
        return self.get_json_api(f'catalog/productstock/{product_id}', params=params)

    def get_products_variations(self, **params):
        """Returns all products variations."""
        return self.get_json_api('catalog/productsvariations', params=params)

    def get_products_variations_stock(self, **params):
        """Returns all products variations stock."""
        return self.get_json_api('catalog/productsvariationsstock', params=params)

    def get_products_variations_stock_available(self, **params):
        """Returns all products variations stock available."""
        return self.get_json_api('catalog/productsvariationsstockavailable', params=params)

    def get_product_tags(self, product_id: Id, **params):
        """Get a single ProductTag."""
        return self.get_json_api(f'catalog/producttags/{product_id}', params=params)

    def get_product_variations(self, product_id: Id, **params):
        """Get a single Product variations."""
        return self.get_json_api(f'catalog/productvariations/{product_id}', params=params)

    def get_product_variations_stock(self, product_id: Id, **params):
        """Get a single product variation stock."""
        return self.get_json_api(f'catalog/productvariationsstock/{product_id}', params=params)

    def get_tag(self, tag_id: Id, **params):
        """Get a single tag."""
        return self.get_json_api(f'catalog/tag/{tag_id}', params=params)

    def get_tag_all_languages(self, tag_id: Id, **params):
        """Get a single tag in all languages."""
        return self.get_json_api(f'catalog/tagalllanguages/{tag_id}', params=params)

    def get_tags(self, **params):
        """Lists all tags."""
        return self.get_json_api('catalog/tags', params=params)

    def get_variation(self, variation_id: Id, **params):
        """Get a single variation."""
        return self.get_json_api(f'catalog/variation/{variation_id}', params=params)

    def get_variations(self, **params):
        """Lists all variations."""
        return self.get_json_api('catalog/variations', params=params)

    # shipping
    def get_carriers(self, **params):
        """Get a single variation."""
        return self.get_json_api('shipping/carriers', params=params)

    def get_shipping_order(self, order: Dict[str, Any]):
        """Get the list of available shipping options with the calculated weight and cost in Kg and € respectively,
        for the given order.

        Example order:
            {"delivery":{"isoCountry":"ES","postcode":"46005"},"products":[{"reference":"V1300179","quantity":1}]}
        """
        if "order" in order:
            warnings.warn("Calling get_shipping_order({\"order\": order}) is deprecated;"
                          " use get_shipping_order(order) instead.",
                          DeprecationWarning)
            order_payload = order
        else:
            order_payload = {"order": order}
        return self.post_api('shipping/orders', json=order_payload).json()

    # order
    def get_order_addresses(self, **params):
        """
        Get order shipping address structure.
        Note this endpoint has been removed on 2022/05/25.
        """
        return self.get_json_api('order/addresses/new', **params)

    def get_order_carriers(self, **params):
        """
        Get order shipping address structure.
        Note this endpoint has been removed on 2022/05/25.
        """
        return self.get_json_api('order/carriers/new', **params)

    def check_order(self, order: Dict[str, Any], **params):
        """Check/simulate an order and return the total order to paid.

        Example order:

        {
          "internalReference": "123456",
          "language": "es",
          "paymentMethod": "moneybox",
          "carriers": [
            {
              "name": "correos"
            },
            {
              "name": "chrono"
            }
          ],
          "shippingAddress": {
            "firstName": "John",
            "lastName": "Doe",
            "country": "ES",
            "postcode": "46005",
            "town": "Valencia",
            "address": "C/ Altea",
            "phone": "664869570",
            "email": "john@email.com",
            "comment": ""
          },
          "products": [
            {
              "reference": "F1505138",
              "quantity": 4
            }
          ]
        }
        """
        if "order" in order:
            warnings.warn("Calling check_order({\"order\": order}) is deprecated; use check_order(order) instead.",
                          DeprecationWarning)
            order_payload = order
        else:
            order_payload = {"order": order}
        return self.post_api('order/check', json=order_payload, **params).json()

    def create_order(self, order: Dict[str, Any], **params):
        """
        Submit an order.

        Example order:
        order = {
          "internalReference": "123456",
          "language": "es",
          "paymentMethod": "moneybox",
          "carriers": [
            {
              "name": "correos"
            },
            {
              "name": "chrono"
            }
          ],
          "shippingAddress": {
            "firstName": "John",
            "lastName": "Doe",
            "country": "ES",
            "postcode": "46005",
            "town": "Valencia",
            "address": "C/ Altea",
            "phone": "664869570",
            "email": "john@email.com",
            "comment": ""
          },
          "products": [
            {
              "reference": "F1505138",
              "quantity": 4
            }
          ]
        }
        """
        if "order" in order:
            warnings.warn("Calling create_order({\"order\": order}) is deprecated; use create_order(order) instead.",
                          DeprecationWarning)
            order_payload = order
        else:
            order_payload = {"order": order}
        # NOTE(BF): we must return the raw response because we need the headers to parse 'Location'
        return self.post_api('order/create', json=order_payload, **params)

    def create_order_id(self, order: dict, **params) -> str:
        """Like create_order(), but return the order id."""
        response = self.create_order(order, **params)
        # Format:
        # {
        #     'Content-Length': '0',
        #     'Content-Type': 'application/json',
        #     'Date': 'Thu, 09 Apr 2020 07:24:56 GMT',
        #     'Location': '/rest/order/119...',
        #     'Set-Cookie': 'secure_key=16...065; expires=Thu, 16-Apr-2020 07:24:56 GMT; Max-Age=604800; path=/',
        # }
        # the id of the bigbuy order is only known in the location url in the headers
        order_id = response.headers["Location"].replace("/rest/order/", "")
        return order_id

    def get_order_by_customer_reference(self, reference: str, **params):
        """Get order information by customer reference."""
        return self.get_json_api(f'order/reference/{reference}', **params)

    def get_order_by_id(self, order_id: Union[str, int], **params):
        """Get order information."""
        return self.get_json_api(f'order/{order_id}', **params)

    # tracking
    def get_tracking_carriers(self, **params):
        """Get the list of available carriers."""
        return self.get_json_api('tracking/carriers', **params)

    def get_tracking_order(self, order_id: Id, **params):
        """Get the list of available trackings."""
        return self.get_json_api(f'tracking/order/{order_id}', **params)

    def get_tracking_orders(self, order_ids: Iterable[Id], match_ids=True, **params) -> List[Optional[dict]]:
        """
        Get the list of available trackings for the given orders.

        If ``match_ids`` is true (the default), the returned sequence is guaranteed to have the same length
        as ``order_ids``, filled with ``None`` when appropriate. Otherwise it should be in the same order but may
        be shorter as some orders may not have available tracking.
        """
        payload = {
            "track": {
                "orders": [{"id": order_id} for order_id in order_ids],
            }
        }

        trackings = cast(List[dict], self.post_api('tracking/orders', json=payload, **params).json())

        if not match_ids:
            # make mypy happy
            return cast(List[Optional[dict]], trackings)

        tracking_by_id: Dict[str, dict] = {}
        for tracking in trackings:
            tracking_by_id[str(tracking["id"])] = tracking

        return [tracking_by_id.get(str(order_id)) for order_id in order_ids]

    def get_lowest_shipping_cost_by_country(self, reference: str, country_code: str, **params) -> dict:
        """
        Equivalent of ``get_lowest_shipping_costs_by_country`` for a single product. Returns the lowest shipping cost
        for a product reference when sent to the provided country.

        Example response:

            {
                "shippingCost": "4.3",
                "carrier": {
                    "id": "43",
                    "name": "Chrono"
                }
            }
        """
        return self.post_api("shipping/lowest-shipping-cost-by-country",
                             json={"product_country": {"reference": reference, "countryIsoCode": country_code}},
                             **params).json()

    def get_lowest_shipping_costs_by_country(self, country_code: str, **params) -> List[dict]:
        """
        Returns the lowest shipping cost for a product reference when sent to the provided country.

        As of 2022/04/21 the information is available for the following countries:
           FR, DK, CY, HU, GB, LT, MT, ES, LV, SK, RO, US, FI, GR, CZ, HR, SE, IE, LU, NL, AU, BG, NO, IT, DE, SI, PL,
           BE, CH, EE, PT, AT.
        """
        return self.get_json_api(f"shipping/lowest-shipping-costs-by-country/{country_code}", **params)

    def get_purse_amount(self, **params):
        """
        Get the amount of money available in the purse.
        """
        return float(self.get_json_api("user/purse", **params))

    def get_modules(self, **params):
        """
        Get all modules.
        """
        return self.get_json_api("module/", **params)

    def get_module_platforms(self, **params):
        """
        Get all module platforms.
        """
        return self.get_json_api("module/platforms", **params)

    def get_taxonomies(self, **params) -> List[dict]:
        """
        List all taxonomies.
        """
        return self.get_json_api("catalog/taxonomies", **params)

    def get_taxonomy_all_languages(self, taxonomy_id: Id, **params):
        """
        Get a single taxonomy in all languages.
        """
        return self.get_json_api(f"catalog/taxonomyalllanguages/{taxonomy_id}", **params)

    def get_product_taxonomies(self, product_id: Id, **params) -> Optional[List[dict]]:
        """
        Return all taxonomies associated with a product.

        Example:

            [{'id': 5906, 'taxonomy': 5906, 'product': 334497}, {'id': 5908, 'taxonomy': 5908, 'product': 334497}]
        """
        return self.get_json_api(f"catalog/producttaxonomies/{product_id}", **params)

    def get_products_taxonomies(self, **params) -> List[dict]:
        """
        Return all taxonomies of all products.
        The format is the same as ``get_product_taxonomies``
        """
        return self.get_json_api(f"catalog/productstaxonomies", **params)
