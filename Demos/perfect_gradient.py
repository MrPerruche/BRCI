import brci

from os import system  # for 'pause'


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def interpolate_hue(hue_start, hue_end, progress, long_way=False):
    """Interpolate hue with short or long path option."""
    diff = hue_end - hue_start
    if abs(diff) > 180:
        # Wrap around for short path, or go long path if specified
        hue_end += 360 if (diff < 0) == long_way else -360  # Wizardry here. Ask chatgpt about it, he wrote it.
    return lerp(hue_start, hue_end, progress)


if __name__ == '__main__':

    str1: str = (brci.inputr(f"What color is your first gradient (as #{brci.FM.RED}RR{brci.FM.GREEN}GG{brci.FM.BLUE}BB{brci.FM.CLEAR_ALL})?\n> ")
                 .replace('#', '')
                 .replace(' ', ''))
    assert len(str1) == 6, f"Expected 6 chars, not {len(str1)}"  # Right length
    assert set(str1) - set('0123456789abcdefABCDEF') == set(), f"Expected only hex chars, found {set(str1) - set('0123456789abcdef')}."
    col1: list[int] = [int(str1[i:i+2], 16) for i in range(0, len(str1), 2)]
    oklch1: list[float] = brci.rgb_to_oklch(*col1)
    print('Valid Input.')

    str2: str = (brci.inputr(f"What color is your second gradient (as #{brci.FM.RED}RR{brci.FM.GREEN}GG{brci.FM.BLUE}BB{brci.FM.CLEAR_ALL})?\n> ")
                 .replace('#', '')
                 .replace(' ', ''))
    assert len(str2) == 6, f"Expected 6 chars, not {len(str2)}"  # Right length
    assert set(str2) - set('0123456789abcdefABCDEF') == set(), f"Expected only hex chars, found {set(str2) - set('0123456789abcdef')}."
    col2: list[int] = [int(str2[i:i+2], 16) for i in range(0, len(str2), 2)]
    oklch2: list[float] = brci.rgb_to_oklch(*col2)
    print('Valid Input.')

    short: bool = brci.inputr(f"Use short path? (y/N)\n> ").lower().strip().startswith('y')
    print(f"{'Short' if short else 'Long'} interpolation will be used.")

    div: int = int(input('Into how many bricks would you like?\n> '))
    assert div >= 2, 'You must have at least 2 bricks for the two original colors.'
    brci.printr(f"Valid input. Generating a {div} bricks gradient using OKLCH...", col=brci.FM.LIGHT_GREEN)


    creation: brci.ModernCreation = brci.Creation15(
        'demo_perfect_gradient',
        brci.Creation15.get_brick_rigs_vehicle_folder(),
        name=f"Demo perfect gradient",
        description=f"Demo of a perfect gradient going in a straight line. Created using brci-{brci.BRCI_VERSION}.",
        author=76561199130146863,  # SteamID 64 of Perru_
        size=brci.Creation15.Value().metadata_size(0.3 * div, 0.3, 0.1, unit=brci.Units.METER)
    )

    for i in range(div):
        progress = i / (div - 1)
        mid_color = [
            lerp(oklch1[0], oklch2[0], progress),
            lerp(oklch1[1], oklch2[1], progress),
            interpolate_hue(oklch1[2], oklch2[2], progress, long_way=True)
        ]

        creation.add_brick(
            'ScalableBrick',
            f'perfect_gradient.brick{i}',
            brci.Creation15.Value().position(i*0.3, 0, 0, unit=brci.Units.METER),
            [0, 0, 0],
            {
                "BrickSize": brci.Creation15.Value().size(0.3, 0.3, 0.03, unit=brci.Units.METER),
                "BrickColor": brci.linear_to_srgb(*brci.Creation15.Value().from_oklch(*mid_color)),
                "BrickMaterial": brci.Creation15.Value().Material.OAK
            }
        )


    creation.write_creation()
    creation.write_metadata()
    creation.write_preview(brci.BRCI_THUMBNAIL)

    brci.printr("Near-perfect gradient created successfully.", col=brci.FM.LIGHT_GREEN)
    system('pause')