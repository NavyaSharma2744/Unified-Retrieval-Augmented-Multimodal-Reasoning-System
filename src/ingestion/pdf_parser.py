from pathlib import Path
import fitz  # PyMuPDF


class PDFParser:
    def __init__(self, pdf_path: str):
        """
        Initialize the parser with a PDF path.

        Args:
            pdf_path: Path to the input PDF file.
        """
        self.pdf_path = Path(pdf_path)

        if not self.pdf_path.exists():
            raise FileNotFoundError(f"PDF not found: {self.pdf_path}")

        self.doc = fitz.open(self.pdf_path)

    def extract_text(self) -> list[dict]:
        """
        Extract text from each page of the PDF.

        Returns:
            A list of dictionaries, one per page:
            [
                {
                    "page_number": 1,
                    "text": "..."
                },
                ...
            ]
        """
        pages = []

        for page_index, page in enumerate(self.doc):
            text = page.get_text("text").strip()

            pages.append(
                {
                    "page_number": page_index + 1,
                    "text": text,
                }
            )

        return pages

    def extract_images(self, output_dir: str = "data/interim/extracted_images") -> list[dict]:
        """
        Extract images from the PDF and save them to disk.

        Args:
            output_dir: Directory where extracted images will be stored.

        Returns:
            A list of dictionaries describing saved images:
            [
                {
                    "page_number": 1,
                    "image_index": 0,
                    "image_path": "..."
                },
                ...
            ]
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        extracted_images = []

        for page_index in range(len(self.doc)):
            page = self.doc[page_index]
            images = page.get_images(full=True)

            for image_index, img in enumerate(images):
                xref = img[0]
                base_image = self.doc.extract_image(xref)

                image_bytes = base_image["image"]
                image_ext = base_image["ext"]

                image_filename = f"{self.pdf_path.stem}_page{page_index + 1}_img{image_index}.{image_ext}"
                image_path = output_path / image_filename

                with open(image_path, "wb") as f:
                    f.write(image_bytes)

                extracted_images.append(
                    {
                        "page_number": page_index + 1,
                        "image_index": image_index,
                        "image_path": str(image_path),
                    }
                )

        return extracted_images

    def close(self) -> None:
        """Close the opened PDF document."""
        self.doc.close()
