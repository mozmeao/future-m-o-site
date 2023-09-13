# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Generated by Django 4.1.10 on 2023-07-27 14:39

import django.db.models.deletion
from django.db import migrations, models

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("wagtailcore", "0083_workflowcontenttype"),
        ("microsite", "0056_alter_footer_aftermatter_alter_footer_columns_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogindexpage",
            name="read_more_cta_label",
            field=models.CharField(
                default="Read more",
                help_text="Only shown if you mark a post as featured",
                max_length=50,
                verbose_name="Featured Post CTA button label",
            ),
        ),
        migrations.CreateModel(
            name="LongformArticlePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "page_layout",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("mzp-l-content mzp-t-content-sm", "Small"),
                            ("mzp-l-content mzp-t-content-md", "Medium"),
                            ("mzp-l-content mzp-t-content-lg", "Large"),
                            ("mzp-l-content mzp-t-content-xl", "Extra Large"),
                        ],
                        default="mzp-l-content mzp-t-content-lg",
                        help_text="Optional layout wrapper <i>– only for components that need one</i>. <a href='https://protocol.mozilla.org/components/detail/content-container--default.html'>Protocol docs for layout</a>.",
                        max_length=64,
                    ),
                ),
                (
                    "menu_description",
                    models.CharField(blank=True, help_text="Text to accompany an entry in the navigation menu. Optional.", max_length=200),
                ),
                ("introduction", wagtail.fields.RichTextField(blank=True, help_text="Optional intro for the page")),
                (
                    "content",
                    wagtail.fields.StreamField(
                        [
                            (
                                "text",
                                wagtail.blocks.RichTextBlock(
                                    features=["h2", "h3", "bold", "italic", "strikethrough", "code", "blockquote", "link", "ol", "ul"], required=False
                                ),
                            ),
                            (
                                "image",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("image", wagtail.images.blocks.ImageChooserBlock(required=False)),
                                        ("alt_text", wagtail.blocks.CharBlock(label="Alt-text for this image", max_length=250, required=False)),
                                        (
                                            "decorative_only",
                                            wagtail.blocks.BooleanBlock(default=False, label="Is this image decorative only?", required=False),
                                        ),
                                        (
                                            "width",
                                            wagtail.blocks.IntegerBlock(label="Specific image width in px (optional)", min_value=0, required=False),
                                        ),
                                        (
                                            "height",
                                            wagtail.blocks.IntegerBlock(label="Specific image height in px (optional)", min_value=0, required=False),
                                        ),
                                        (
                                            "rendition_spec",
                                            wagtail.blocks.CharBlock(
                                                blank=True,
                                                default="original",
                                                help_text="Lots of options available. See <a href='https://docs.wagtail.org/en/stable/topics/images.html#available-resizing-methods'>Wagtail docs on image sizing</a> Defaults to 'original'",
                                                max_length=256,
                                            ),
                                        ),
                                        ("image_caption", wagtail.blocks.CharBlock(max_length=250, required=False)),
                                        ("image_credit", wagtail.blocks.CharBlock(max_length=250, required=False)),
                                    ],
                                    label_format="Captioned image: {image_caption}",
                                    required=False,
                                ),
                            ),
                            (
                                "callout",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("headline", wagtail.blocks.CharBlock(help_text="Around 50 chars", max_length=50, required=True)),
                                        ("body", wagtail.blocks.TextBlock(help_text="Around 150 chars", max_length=180, required=True)),
                                        (
                                            "cta",
                                            wagtail.blocks.StructBlock(
                                                [
                                                    ("page", wagtail.blocks.PageChooserBlock(label="Page", required=False)),
                                                    ("external_url", wagtail.blocks.URLBlock(label="External URL", required=False)),
                                                    ("button_text", wagtail.blocks.CharBlock(max_length=50, required=False)),
                                                ],
                                                required=True,
                                            ),
                                        ),
                                        ("theme", wagtail.blocks.ChoiceBlock(choices=[("mzp-t-light", "Light theme"), ("mzp-t-dark", "Dark theme")])),
                                    ],
                                    help_text="<a href='https://protocol.mozilla.org/components/detail/compact-call-out--default.html'>Protocol docs for compact-callout</a>.",
                                    label_format="Compact callout: {headline}",
                                    required=False,
                                ),
                            ),
                        ],
                        blank=True,
                        use_json_field=True,
                    ),
                ),
                (
                    "menu_icon",
                    models.ForeignKey(
                        blank=True,
                        help_text="Icon to accompany an entry in the navigation menu. Optional.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]