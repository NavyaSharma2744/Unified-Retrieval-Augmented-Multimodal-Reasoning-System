from pathlib import Path
import fitz  # PyMuPDF


class PDFParser:
    def __init__(self, pdf_path: str):
        self.pdf_path = Path(pdf_path)
        if not self.pdf_path.exists():
            raise FileNotFoundError(f"PDF not found: {self.pdf_path}")
        self.doc = fitz.open(str(self.pdf_path))

    def extract_text(self) -> list[dict]:
        pages = []
        for i, page in enumerate(self.doc):
            text = page.get_text("text").strip()
            pages.append(
                {
                    "page_number": i + 1,
                    "text": text,
                    "source_pdf": self.pdf_path.name,
                }
            )
        return pages

    def extract_images(self, output_dir: str = "data/interim/extracted_images") -> list[dict]:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        extracted = []

        for page_index in range(len(self.doc)):
            page = self.doc[page_index]
            images = page.get_images(full=True)

            for img_index, img in enumerate(images):
                xref = img[0]
                base_image = self.doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]

                image_filename = f"{self.pdf_path.stem}_page{page_index + 1}_img{img_index + 1}.{image_ext}"
                image_file = output_path / image_filename

                with open(image_file, "wb") as f:
                    f.write(image_bytes)

                extracted.append(
                    {
                        "page_number": page_index + 1,
                        "image_index": img_index + 1,
                        "image_path": str(image_file),
                        "source_pdf": self.pdf_path.name,
                    }
                )

        return extracted

    def close(self) -> None:
        self.doc.close()
