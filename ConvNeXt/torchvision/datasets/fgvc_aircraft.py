from __future__ import annotations

import os
from typing import Any, Callable, Optional, Tuple

import PIL.Image

from .utils import download_and_extract_archive, verify_str_arg
from .vision import VisionDataset


class FGVCAircraft(VisionDataset):
    """`FGVC Aircraft <https://www.robots.ox.ac.uk/~vgg/data/fgvc-aircraft/>`_ Dataset.

    The dataset contains 10,200 images of aircraft, with 100 images for each of 102
    different aircraft model variants, most of which are airplanes.
    Aircraft models are organized in a three-levels hierarchy. The three levels, from
    finer to coarser, are:

    - ``variant``, e.g. Boeing 737-700. A variant collapses all the models that are visually
        indistinguishable into one class. The dataset comprises 102 different variants.
    - ``family``, e.g. Boeing 737. The dataset comprises 70 different families.
    - ``manufacturer``, e.g. Boeing. The dataset comprises 41 different manufacturers.

    Args:
        root (string): Root directory of the FGVC Aircraft dataset.
        split (string, optional): The dataset split, supports ``train``, ``val``,
            ``trainval`` and ``test``.
        annotation_level (str, optional): The annotation level, supports ``variant``,
            ``family`` and ``manufacturer``.
        transform (callable, optional): A function/transform that  takes in an PIL image
            and returns a transformed version. E.g, ``transforms.RandomCrop``
        target_transform (callable, optional): A function/transform that takes in the
            target and transforms it.
        download (bool, optional): If True, downloads the dataset from the internet and
            puts it in root directory. If dataset is already downloaded, it is not
            downloaded again.
    """

    _URL = "https://www.robots.ox.ac.uk/~vgg/data/fgvc-aircraft/archives/fgvc-aircraft-2013b.tar.gz"

    def __init__(
        self,
        root: str,
        split: str = "trainval",
        annotation_level: str = "variant",
        transform: Optional[Callable] = None,
        target_transform: Optional[Callable] = None,
        download: bool = False,
    ) -> None:
        super().__init__(root, transform=transform, target_transform=target_transform)
        self._split = verify_str_arg(split, "split", ("train", "val", "trainval", "test"))
        self._annotation_level = verify_str_arg(
            annotation_level, "annotation_level", ("variant", "family", "manufacturer")
        )

        self._data_path = os.path.join(self.root, "fgvc-aircraft-2013b")
        if download:
            self._download()

        if not self._check_exists():
            raise RuntimeError("Dataset not found. You can use download=True to download it")

        # annotation_file = os.path.join(
        #     self._data_path,
        #     "data",
        #     {
        #         "variant": "variants.txt",
        #         "family": "families.txt",
        #         "manufacturer": "manufacturers.txt",
        #     }[self._annotation_level],
        # )
        # with open(annotation_file, "r") as f:
        #     self.classes = [line.strip() for line in f]

        # self.class_to_idx = dict(zip(self.classes, range(len(self.classes))))

        # image_data_folder = os.path.join(self._data_path, "data", "images")
        # labels_file = os.path.join(self._data_path, "data", f"images_{self._annotation_level}_{self._split}.txt")

        # self._image_files = []
        # self._labels = []

        # with open(labels_file, "r") as f:
        #     for line in f:
        #         image_name, label_name = line.strip().split(" ", 1)
        #         self._image_files.append(os.path.join(image_data_folder, f"{image_name}.jpg"))
        #         self._labels.append(self.class_to_idx[label_name])

        annotation_level = "variant"

        annotation_file = os.path.join(
            self._data_path,
            "data",
            {
                "variant": "variants.txt",
                "family": "families.txt",
                "manufacturer": "manufacturers.txt",
            }[annotation_level],
        )

        with open(annotation_file, "r") as f:
            self.classes = [line.strip() for line in f]

        self.class_to_idx = dict(zip(self.classes, range(len(self.classes))))

        image_data_folder = os.path.join(self._data_path, "data", "images")
        labels_file = os.path.join(self._data_path, "data", f"images_{annotation_level}_{self._split}.txt")

        self._image_files = []
        self._labels_variant = []

        with open(labels_file, "r") as f:
            for line in f:
                image_name, label_name = line.strip().split(" ", 1)
                self._image_files.append(os.path.join(image_data_folder, f"{image_name}.jpg"))
                self._labels_variant.append(self.class_to_idx[label_name])


        annotation_level = "family"

        annotation_file = os.path.join(
            self._data_path,
            "data",
            {
                "variant": "variants.txt",
                "family": "families.txt",
                "manufacturer": "manufacturers.txt",
            }[annotation_level],
        )

        with open(annotation_file, "r") as f:
            self.classes = [line.strip() for line in f]

        self.class_to_idx = dict(zip(self.classes, range(len(self.classes))))

        image_data_folder = os.path.join(self._data_path, "data", "images")
        labels_file = os.path.join(self._data_path, "data", f"images_{annotation_level}_{self._split}.txt")

        self._image_files = []
        self._labels_family = []

        with open(labels_file, "r") as f:
            for line in f:
                image_name, label_name = line.strip().split(" ", 1)
                self._image_files.append(os.path.join(image_data_folder, f"{image_name}.jpg"))
                self._labels_family.append(self.class_to_idx[label_name])

        
        annotation_level = "manufacturer"

        annotation_file = os.path.join(
            self._data_path,
            "data",
            {
                "variant": "variants.txt",
                "family": "families.txt",
                "manufacturer": "manufacturers.txt",
            }[annotation_level],
        )

        with open(annotation_file, "r") as f:
            self.classes = [line.strip() for line in f]

        self.class_to_idx = dict(zip(self.classes, range(len(self.classes))))

        image_data_folder = os.path.join(self._data_path, "data", "images")
        labels_file = os.path.join(self._data_path, "data", f"images_{annotation_level}_{self._split}.txt")

        self._image_files = []
        self._labels_manufacturer = []

        with open(labels_file, "r") as f:
            for line in f:
                image_name, label_name = line.strip().split(" ", 1)
                self._image_files.append(os.path.join(image_data_folder, f"{image_name}.jpg"))
                self._labels_manufacturer.append(self.class_to_idx[label_name])

        

    def __len__(self) -> int:
        return len(self._image_files)

    def __getitem__(self, idx) -> Tuple[Any, Any]:
        image_file, label_variant, labels_family, labels_manufacturer = self._image_files[idx], \
                                                        self._labels_variant[idx], self._labels_family[idx], self._labels_manufacturer[idx]
        image = PIL.Image.open(image_file).convert("RGB")

        if self.transform:
            image = self.transform(image)

        if self.target_transform:
            label_variant = self.target_transform(label_variant)
            labels_family = self.target_transform(labels_family)
            labels_manufacturer = self.target_transform(labels_manufacturer)

        return image, [label_variant, labels_family, labels_manufacturer]

        # image_file, label = self._image_files[idx], self._labels[idx]
        # image = PIL.Image.open(image_file).convert("RGB")

        # if self.transform:
        #     image = self.transform(image)

        # if self.target_transform:
        #     label = self.target_transform(label)

        # return image, label

    def _download(self) -> None:
        """
        Download the FGVC Aircraft dataset archive and extract it under root.
        """
        if self._check_exists():
            return
        download_and_extract_archive(self._URL, self.root)

    def _check_exists(self) -> bool:
        return os.path.exists(self._data_path) and os.path.isdir(self._data_path)
