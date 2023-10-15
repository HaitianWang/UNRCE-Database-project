# Generated by Django 4.2.4 on 2023-09-21 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="ESD",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Organisation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("org_name", models.CharField(max_length=255, unique=True)),
                ("address", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="PriorityArea",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField(default="Default Title")),
                (
                    "project_cover_image",
                    models.FileField(
                        blank=True, null=True, upload_to="project_images/"
                    ),
                ),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("concluded_on", models.DateTimeField(blank=True, null=True)),
                (
                    "audience",
                    models.CharField(
                        choices=[
                            ("general", "General public (any age)"),
                            ("target", "Particular target Audience (Please specify)"),
                            ("adults", "Adults"),
                            ("tertiary", "Tertiary students"),
                            ("high_school", "High school age"),
                            ("primary_school", "Primary School age"),
                            ("early_years", "Early years"),
                            ("adults_60", "Adults >60 please"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "delivery_frequency",
                    models.CharField(
                        choices=[
                            ("monthly", "Monthly"),
                            ("quarterly", "Quarterly"),
                            ("biannually", "Biannually"),
                            ("annually", "Annually"),
                            ("ongoing", "Ongoing"),
                            ("once", "Once"),
                            ("irregular", "Opportunistic/Irregularly"),
                            ("on_demand", "Permanent/On demand"),
                        ],
                        max_length=20,
                    ),
                ),
                ("language", models.TextField()),
                ("format", models.TextField()),
                ("web_link", models.URLField()),
                ("policy_link", models.URLField()),
                ("results", models.TextField(blank=True, max_length=150)),
                ("lessons_learned", models.TextField(blank=True, max_length=100)),
                ("key_messages", models.CharField(blank=True, max_length=50)),
                ("relationship_to_rce_activities", models.TextField(blank=True)),
                ("funding", models.TextField(blank=True)),
                (
                    "affiliations",
                    models.ManyToManyField(
                        related_name="affiliated_projects", to="UNRCE_APP.organisation"
                    ),
                ),
                (
                    "contributing_organizations",
                    models.ManyToManyField(
                        related_name="contributing_projects",
                        to="UNRCE_APP.organisation",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RCEHub",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("hub_name", models.CharField(max_length=255)),
                ("contact_info", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="SDG",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sdg",
                    models.CharField(
                        choices=[
                            ("goal_1", "End poverty in all its forms everywhere"),
                            (
                                "goal_2",
                                "End hunger, achieve food security and improved nutrition and promote sustainable agriculture",
                            ),
                            (
                                "goal_3",
                                "Ensure healthy lives and promote well-being for all at all ages",
                            ),
                            (
                                "goal_4",
                                "Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all",
                            ),
                            (
                                "goal_5",
                                "Achieve gender equality and empower all women and girls",
                            ),
                            (
                                "goal_6",
                                "Ensure availability and sustainable management of water and sanitation for all",
                            ),
                            (
                                "goal_7",
                                "Ensure access to affordable, reliable, sustainable and modern energy for all",
                            ),
                            (
                                "goal_8",
                                "Promote sustained, inclusive and sustainable economic growth, full and productive employment and decent work for all",
                            ),
                            (
                                "goal_9",
                                "Build resilient infrastructure, promote inclusive and sustainable industrialization and foster innovation",
                            ),
                            ("goal_10", "Reduce inequality within and among countries"),
                            (
                                "goal_11",
                                "Make cities and human settlements inclusive, safe, resilient and sustainable",
                            ),
                            (
                                "goal_12",
                                "Ensure sustainable consumption and production patterns",
                            ),
                            (
                                "goal_13",
                                "Take urgent action to combat climate change and its impacts",
                            ),
                            (
                                "goal_14",
                                "Conserve and sustainably use the oceans, seas and marine resources for sustainable development",
                            ),
                            (
                                "goal_15",
                                "Protect, restore and promote sustainable use of terrestrial ecosystems, sustainably manage forests, combat desertification, and halt and reverse land degradation and halt biodiversity loss",
                            ),
                            (
                                "goal_16",
                                "Promote peaceful and inclusive societies for sustainable development, provide access to justice for all and build effective, accountable and inclusive institutions at all levels",
                            ),
                            (
                                "goal_17",
                                "Strengthen the means of implementation and revitalize the Global Partnership for Sustainable Development",
                            ),
                        ],
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ProjectSDG",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "relationship_type",
                    models.CharField(
                        choices=[("direct", "Direct"), ("indirect", "Indirect")],
                        max_length=10,
                    ),
                ),
                (
                    "goal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="UNRCE_APP.sdg"
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UNRCE_APP.project",
                    ),
                ),
            ],
            options={
                "unique_together": {("project", "goal")},
            },
        ),
        migrations.CreateModel(
            name="ProjectPriorityArea",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "relationship_type",
                    models.CharField(
                        choices=[("direct", "Direct"), ("indirect", "Indirect")],
                        max_length=10,
                    ),
                ),
                (
                    "priority_area",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UNRCE_APP.priorityarea",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UNRCE_APP.project",
                    ),
                ),
            ],
            options={
                "unique_together": {("project", "priority_area")},
            },
        ),
        migrations.CreateModel(
            name="ProjectImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UNRCE_APP.project",
                    ),
                ),
                (
                    "project_cover_image",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="UNRCE_APP.projectimage",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProjectFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="project_files/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UNRCE_APP.project",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProjectESD",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "relationship_type",
                    models.CharField(
                        choices=[("direct", "Direct"), ("indirect", "Indirect")],
                        max_length=10,
                    ),
                ),
                (
                    "esd",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="UNRCE_APP.esd"
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UNRCE_APP.project",
                    ),
                ),
            ],
            options={
                "unique_together": {("project", "esd")},
            },
        ),
        migrations.AddField(
            model_name="project",
            name="esds",
            field=models.ManyToManyField(
                through="UNRCE_APP.ProjectESD", to="UNRCE_APP.esd"
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="files",
            field=models.ManyToManyField(
                related_name="projects", to="UNRCE_APP.projectfile"
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="priority_areas",
            field=models.ManyToManyField(
                through="UNRCE_APP.ProjectPriorityArea", to="UNRCE_APP.priorityarea"
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="sdgs",
            field=models.ManyToManyField(
                through="UNRCE_APP.ProjectSDG", to="UNRCE_APP.sdg"
            ),
        ),
        migrations.AddField(
            model_name="organisation",
            name="hub",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="UNRCE_APP.rcehub"
            ),
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=60)),
                ("image", models.ImageField(max_length=36, upload_to="")),
                ("uploaded_date", models.DateTimeField()),
                (
                    "uploaded_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Follow",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "followed_project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UNRCE_APP.project",
                    ),
                ),
                (
                    "following_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
