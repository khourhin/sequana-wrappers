from os import sysconf_names
from snakemake.shell import shell
from pathlib import Path

options = snakemake.params.get("options", "")

input_str = " ".join([f"--{k} {','.join(snakemake.input.get(k))}" for k in snakemake.input.keys()])

seqtype = snakemake.params.get("seqtype")
libtype = snakemake.params.get("libtype")

outdir = Path(snakemake.output[0]).parent

logs = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    f"Trinity {input_str} --CPU {snakemake.threads} "
    f" --max_memory {snakemake.resources.mem} --seqType {seqtype} --SS_lib_type {libtype}"
    f" --output {outdir} {snakemake.params.options} "
    f" {logs}"
)

# # Trinity release v2.14.0 changed its path for the output
# new_trinity_fasta = outdir.parent / (str(outdir.stem) + ".Trinity.fasta")
# new_gene_trans_map = outdir.parent / (str(outdir.stem) + ".Trinity.fasta.gene_trans_map")

# if new_trinity_fasta.exists():
#     shell(f"mv {new_trinity_fasta} {outdir / 'Trinity.fasta'}")
#     shell(f"mv {new_gene_trans_map} {outdir / 'Trinity.fasta.gene_trans_map'}")
