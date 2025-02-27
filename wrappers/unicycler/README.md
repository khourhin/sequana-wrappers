# Documentation

This wrapper generates de novo assembly using **Unicycler** an assembly pipeline for bacterial genomes.

**Required input:**

- **fastq**: the input fastq files. Could be short (paired or not) or long reads

**Required output::**

- **contigs**: the contigs fasta file.
 
**Required parameters:**

- **mode**: Bridging mode. (conservative|normal|bold) (default: "normal")
- **options**: a list of valid **Unicycler** options.

**Optional parameters:**

- **long_reads** if provided and set to True, unicycler is used for long reads.
  expected input is therefore single end data (one file).

Notes: This wrapper cannot be used to perform correction only.

**Log:**

- a log file generated by **Unicycler** is created.


# Configuration


    ##############################################################################
    # Unicycler assembly
    #
    # :Parameters:
    #
    # - mode: any bridging mode in this list ["conservative", "normal", "bold"]
    # - options: any options recognised by unicycler cli.
    # - threads: number of threads to be used.
    # - long_reads: set to True to switch to long read analysis
    #
    unicycler:
        mode: "normal"
        long_reads: True # optional
        options: ""
        threads: 4


# Example

    rule unicycler:
        input:
            fastq="data/raw.fastq.gz",
        output:
            contigs="assembled/contigs.fasta",
        params:
            mode=config["unicycler"]["mode"],
            options=config["unicycler"]["options"],
        log:
            "logs/unicycler.log"
        threads:
            config["unicycler"]["threads"]
        container: 
        wrapper:
            "main/wrappers/unicycler"

