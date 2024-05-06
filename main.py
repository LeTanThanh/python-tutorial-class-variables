from html_document import HtmlDocument

if __name__ == "__main__":
  # Introduction to the Python class variables

  # print(HtmlDocument.__name__)
  # print(type(HtmlDocument))
  # print(isinstance(HtmlDocument, type))

  # Get the values of class variables

  # extension = HtmlDocument.extension
  # print(extension)

  # version = HtmlDocument.version
  # print(version)

  # HtmlDocument.media_type
  # AttributeError

  # extension = getattr(HtmlDocument, "extension")
  # print(extension)

  # version = getattr(HtmlDocument, "version")
  # print(version)

  # media_type = getattr(HtmlDocument, "media_type")
  # AttributeError

  # media_type = getattr(HtmlDocument, "media_type", "text/html")
  # print(media_type)

  # Set values for class variables

  # HtmlDocument.version = 10
  # print(HtmlDocument.version)

  # HtmlDocument.media_type = "text/html"
  # print(HtmlDocument.media_type)

  # setattr(HtmlDocument, "media_type", "text/html")
  # print(HtmlDocument.media_type)

  # Delete class variables

  # print(HtmlDocument.version)
  # delattr(HtmlDocument, "version")

  # HtmlDocument.version
  # AttributeError

  # Class variable storage

  # from pprint import pprint

  # HtmlDocument.media_type = "text/html"
  # pprint(HtmlDocument.__dict__)

  # HtmlDocument.__dict__["released"] = 2008
  # TypeError

  # doc = HtmlDocument.__dict__["__doc__"]  # BAD CODE
  # print(doc)

  # Callable class attributes

  from pprint import pprint

  pprint(HtmlDocument.__dict__["render"])
