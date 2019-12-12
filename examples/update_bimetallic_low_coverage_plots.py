from gaspy_regress.analysis_AP import create_gridplot


# CO2RR
adsorbate = 'CO'
target = -0.67
bandwidth = 0.2
targets = (target-bandwidth, target+bandwidth)
filename = 'low coverage bimetallic map/CO_DFT'
create_gridplot(adsorbate, targets, filename, low_coverage=True)


# HER
adsorbate = 'H'
target = -0.27
bandwidth = 0.2
targets = (target-bandwidth, target+bandwidth)
filename = 'low coverage bimetallic map/H_DFT'
create_gridplot(adsorbate, targets, filename, low_coverage=True)


# NH3 decomposition
adsorbate = 'N'
target = -0.91 / 2      # At 1% ammonia concentration
# target = -0.58 / 2        # At 50% ammonia concentration
bandwidth = 0.2
targets = (target-bandwidth, target+bandwidth)
filename = 'low coverage bimetallic map/N_DFT'
create_gridplot(adsorbate, targets, filename, low_coverage=True)


# ORR (O)
adsorbate = 'O'
target = 2.49
bandwidth = 0.2
targets = (target-bandwidth, target+bandwidth)
filename = 'low coverage bimetallic map/O_DFT'
create_gridplot(adsorbate, targets, filename, low_coverage=True)

# ORR (OH)
adsorbate = 'OH'
target = 1.123
bandwidth = 0.213
targets = (target-bandwidth, target+bandwidth)
filename = 'low coverage bimetallic map/OH_DFT'
create_gridplot(adsorbate, targets, filename, low_coverage=True)

# ORR (OOH)
adsorbate = 'OOH'
target = 4.057
bandwidth = 0.213
targets = (target-bandwidth, target+bandwidth)
filename = 'low coverage bimetallic map/OOH_DFT'
create_gridplot(adsorbate, targets, filename, low_coverage=True)
