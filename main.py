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

  extension = getattr(HtmlDocument, "extension")
  print(extension)

  version = getattr(HtmlDocument, "version")
  print(version)

  # media_type = getattr(HtmlDocument, "media_type")
  # AttributeError

  media_type = getattr(HtmlDocument, "media_type", "text/html")
  print(media_type)
