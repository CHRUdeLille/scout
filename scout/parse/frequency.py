
def parse_frequencies(variant):
    """Add the frequencies to a variant

        Args:
            variant(dict): A parsed vcf variant

        Returns:
            frequencies(dict): A dictionary with the relevant frequencies
    """
    frequencies = {}
    frequencies['thousand_g'] = parse_frequency(variant, '1000GAF')
    frequencies['thousand_g_left'] parse_frequency(variant, 'left_1000GAF')
    frequencies['thousand_g_right'] parse_frequency(variant, 'right_1000GAF')
    frequencies['thousand_g_max'] = parse_frequency(variant, '1000G_MAX_AF')
    frequencies['exac'] = parse_frequency(variant, 'EXACAF')
    frequencies['exac_max'] = parse_frequency(variant, 'ExAC_MAX_AF')

    return frequencies


def parse_frequency(variant, info_key):
    """Parse the thousand genomes frequency"""
    raw_annotation = variant['info_dict'].get(info_key)
    raw_annotation = None if raw_annotation == '.' else raw_annotation
    frequency = float(raw_annotation[0]) if raw_annotation else None
    return frequency
