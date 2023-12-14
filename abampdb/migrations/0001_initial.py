# Generated by Django 4.0.2 on 2023-12-14 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dock_1', models.CharField(max_length=1000, verbose_name='Dock')),
                ('image', models.CharField(max_length=1000, verbose_name='Image')),
                ('global_energy', models.CharField(max_length=1000, verbose_name='Global_Energy')),
                ('attr_vdw', models.CharField(max_length=1000, verbose_name='Attractive_VdW')),
                ('repl_vdw', models.CharField(max_length=1000, verbose_name='Repulsive_VdW')),
                ('binding_energy', models.CharField(max_length=1000, verbose_name='ACE')),
                ('hydrogen_bonding', models.CharField(max_length=1000, verbose_name='HB')),
            ],
        ),
        migrations.CreateModel(
            name='PDBDQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_id', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='PDBQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_id', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='PDBTQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_id', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Targetproteins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('targets', models.CharField(max_length=1000, verbose_name='Targets')),
            ],
        ),
        migrations.CreateModel(
            name='Proteins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amp', models.CharField(max_length=1000, verbose_name='AMP')),
                ('name', models.CharField(max_length=1000, verbose_name='Name')),
                ('sequence', models.CharField(max_length=1000, verbose_name='Sequence')),
                ('hemolytic_activity', models.CharField(max_length=1000, null=True, verbose_name='HemolyticActivity')),
                ('mic_value', models.FloatField(null=True, verbose_name='MICValue')),
                ('solubility', models.CharField(max_length=1000, verbose_name='Solubility')),
                ('tiny', models.IntegerField(null=True, verbose_name='Tiny')),
                ('small', models.IntegerField(null=True, verbose_name='Small')),
                ('aliphatic', models.IntegerField(null=True, verbose_name='Aliphatic')),
                ('aromatic', models.IntegerField(null=True, verbose_name='Aromatic')),
                ('non_polar', models.IntegerField(null=True, verbose_name='NonPolar')),
                ('polar', models.IntegerField(null=True, verbose_name='Polar')),
                ('charged_aa', models.IntegerField(null=True, verbose_name='ChargedAA')),
                ('basic', models.IntegerField(null=True, verbose_name='Basic')),
                ('acidic', models.FloatField(null=True, verbose_name='Acidic')),
                ('mol_weight_tiny', models.FloatField(null=True, verbose_name='MolWeightTiny')),
                ('mol_weight_small', models.FloatField(null=True, verbose_name='MolWeightSmall')),
                ('mol_weight_apliphatic', models.FloatField(null=True, verbose_name='MolWeightAliphatic')),
                ('mol_weight_aromatic', models.FloatField(null=True, verbose_name='MolWeightAromatic')),
                ('mol_weight_non_polar', models.FloatField(null=True, verbose_name='MolWeightNonPolar')),
                ('mol_weight_polar', models.FloatField(null=True, verbose_name='MolWeightPolar')),
                ('mol_weight_charged', models.FloatField(null=True, verbose_name='MolWeightCharged')),
                ('mol_weight_basic', models.FloatField(null=True, verbose_name='MolWeightBasic')),
                ('mol_weight_acidic', models.FloatField(null=True, verbose_name='MolWeightAcidic')),
                ('molecular_weight', models.FloatField(null=True, verbose_name='MolecularWeight')),
                ('length', models.IntegerField(null=True, verbose_name='Length')),
                ('charge', models.FloatField(null=True, verbose_name='Charge')),
                ('p_i', models.FloatField(null=True, verbose_name='pI')),
                ('a_index', models.FloatField(null=True, verbose_name='AIndex')),
                ('instaIndex', models.FloatField(null=True, verbose_name='InstaIndex')),
                ('BomanIndex', models.FloatField(null=True, verbose_name='BomanIndex')),
                ('hydrophobicity', models.FloatField(null=True, verbose_name='Hydrophobicity')),
                ('hmoment_angle', models.FloatField(null=True, verbose_name='HydrophobicMoment')),
                ('transmembrane', models.IntegerField(null=True, verbose_name='Transmembrane')),
                ('extracellular', models.BooleanField(null=True, verbose_name='Extracellular')),
                ('cytoplasmic', models.BooleanField(null=True, verbose_name='Cytoplasmic')),
                ('hydrophobic_plots', models.FloatField(null=True, verbose_name='HydrophobicPlots')),
                ('hydropathy_plots', models.FloatField(null=True, verbose_name='HydropathyPlots')),
                ('disulfide_end', models.CharField(max_length=1000, verbose_name='disulphides')),
                ('toxicity', models.CharField(max_length=1000, null=True, verbose_name='Toxicity')),
                ('rmsf', models.FloatField(null=True, verbose_name='RMSF')),
                ('flexibility', models.FloatField(null=True, verbose_name='Flexibility')),
                ('score', models.IntegerField(null=True, verbose_name='Score')),
                ('pdb_name', models.CharField(max_length=1000, verbose_name='PDBName')),
                ('dock', models.ManyToManyField(related_name='proteins', to='abampdb.Docks')),
                ('target_protein', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='abampdb.targetproteins')),
            ],
        ),
        migrations.AddField(
            model_name='docks',
            name='targets',
            field=models.ManyToManyField(to='abampdb.Targetproteins'),
        ),
    ]
