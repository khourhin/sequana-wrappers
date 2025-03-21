# Documentation

This wrapper generates de novo assembly using **SPAdes**.

**Required input:**

- **fastq**: the input fastq files.

**Required output::**

- **contigs**: the contigs fasta file.
- **scaffolds**: the scaffolds fasta file.
 
**Required parameters:**

- **k**: list of k-mer sizes (must be odd and less than 128). The default is 'auto' mode.
- **preset**: any preset in this list ["meta", "sc", "isolate", "metaplasmid", "metaviral", "rna", "rnaviral"]. Empty by default.
- **options**: a list of valid **SPAdes** options. Some options are incompatible with some preset.
- **memory**: RAM limit for SPAdes in Gb. Make sure this value is correct for the given machine. SPAdes uses the limit value to automatically determine the sizes of various buffers, etc. The wrapper default is 32 Gb.

Notes: This wrapper cannot be used to perform correction only.

**Log:**

- a log file generated by **SPAdes** is created.


# Configuration


    ##############################################################################
    # SPAdes assembly
    #
    # :Parameters:
    #
    # - k: A kmer or list of kmer used to assemble the genome.
    # - preset: any preset in this list ["meta", "sc", "isolate", "metaplasmid", "metaviral", "rna", "rnaviral"]
    # - options: any options recognised by spades.py cli. (do not use --only-error-correction)
    # - threads: number of threads to be used.
    # - memory: memory limit in Gb. 
    #
    spades:
        k: ""
        preset: ""
        options: "--careful"
        threads: 4
        memory: 64


# Example

    rule spades:
        input:
            fastq="data/raw.fastq.gz",
        output:
            contigs="assembled/contigs.fasta",
            scaffolds="assembled/scaffolds.fasta"
        params:
            k=config["spades"]["k"],
            preset=config["spades"]["preset"],
            options=config["spades"]["options"],
            memory=config["spades"]["memory"]
        log:
            "logs/spades.log"
        threads:
            config["spades"]["threads"]
        wrapper:
            "main/wrappers/spades"
