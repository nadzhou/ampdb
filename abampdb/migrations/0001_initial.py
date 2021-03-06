# Generated by Django 4.0.2 on 2022-02-19 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PDBQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Proteins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('sequence', models.CharField(max_length=500, verbose_name='Sequence')),
                ('hydrolitic_activity', models.FloatField(verbose_name='HydrolyticActivity')),
                ('mic_value', models.FloatField(verbose_name='MICValue')),
                ('solubility', models.CharField(max_length=256, verbose_name='Solubility')),
                ('tiny', models.IntegerField(verbose_name='Tiny')),
                ('small', models.IntegerField(verbose_name='Small')),
                ('aliphatic', models.IntegerField(verbose_name='Aliphatic')),
                ('aromatic', models.IntegerField(verbose_name='Aromatic')),
                ('non_polar', models.IntegerField(verbose_name='NonPolar')),
                ('polar', models.IntegerField(verbose_name='Polar')),
                ('charged_aa', models.IntegerField(verbose_name='ChargedAA')),
                ('basic', models.IntegerField(verbose_name='Basic')),
                ('acidic', models.FloatField(verbose_name='Acidic')),
                ('mol_weight_tiny', models.FloatField(verbose_name='MolWeightTiny')),
                ('mol_weight_small', models.FloatField(verbose_name='MolWeightSmall')),
                ('mol_weight_apliphatic', models.FloatField(verbose_name='MolWeightAliphatic')),
                ('mol_weight_aromatic', models.FloatField(verbose_name='MolWeightAromatic')),
                ('mol_weight_non_polar', models.FloatField(verbose_name='MolWeightNonPolar')),
                ('mol_weight_polar', models.FloatField(verbose_name='MolWeightPolar')),
                ('mol_weight_charged', models.FloatField(verbose_name='MolWeightCharged')),
                ('mol_weight_basic', models.FloatField(verbose_name='MolWeightBasic')),
                ('mol_weight_acidic', models.FloatField(verbose_name='MolWeightAcidic')),
                ('molecular_weight', models.FloatField(verbose_name='MolecularWeight')),
                ('length', models.IntegerField(verbose_name='Length')),
                ('charge', models.FloatField(verbose_name='Charge')),
                ('p_i', models.FloatField(verbose_name='pI')),
                ('a_index', models.FloatField(verbose_name='AIndex')),
                ('instaIndex', models.FloatField(verbose_name='InstaIndex')),
                ('BomanIndex', models.FloatField(verbose_name='BomanIndex')),
                ('hydrophobicity', models.FloatField(verbose_name='Hydrophobicity')),
                ('hmoment_angle', models.FloatField(verbose_name='HydrophobicMoment')),
                ('transmembrane', models.IntegerField(verbose_name='Transmembrane')),
                ('extracellular', models.BooleanField(verbose_name='Extracellular')),
                ('cytoplasmic', models.BooleanField(verbose_name='Cytoplasmic')),
                ('hydrophobic_plots', models.FloatField(verbose_name='HydrophobicPlots')),
                ('hydropathy_plots', models.FloatField(verbose_name='HydropathyPlots')),
                ('disulfide_end', models.CharField(max_length=256, verbose_name='DisulfideEnd')),
                ('toxicity', models.CharField(max_length=256, verbose_name='Toxicity')),
                ('rmsf', models.FloatField(verbose_name='RMSF')),
                ('flexibility', models.FloatField(verbose_name='Flexibility')),
                ('pdb_name', models.CharField(max_length=256, verbose_name='PDBName')),
                ('links', models.URLField(blank=True, db_index=True, max_length=128, verbose_name='Links')),
            ],
        ),
    ]
