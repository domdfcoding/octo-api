# stdlib
from typing import Dict

# 3rd party
from pytest_regressions.file_regression import FileRegressionFixture

# this package
from octo_api.api import OctoAPI
from octo_api.pagination import PaginatedResponse
from octo_api.products import DetailedProduct, Product, RegionalTariffs, Tariff, _parse_tariffs


def test_get_products(api: OctoAPI):
	assert isinstance(api.get_products(), PaginatedResponse)
	assert api.get_products()[0] == Product(
			code="1201",
			direction="IMPORT",
			full_name="Affect Standard Tariff",
			display_name="Affect Standard Tariff",
			description="Affect Standard Tariff",
			is_variable=True,
			is_green=False,
			is_tracker=False,
			is_prepay=False,
			is_business=False,
			is_restricted=False,
			term=None,
			available_from="2016-01-01T00:00:00Z",
			available_to=None,
			brand="AFFECT_ENERGY",
			links=[{
					"href": "https://api.octopus.energy/v1/products/1201/",
					"rel": "self",
					"method": "GET",
					}]
			)

	assert api.get_products(is_green=True)[0] == Product(
			code="AGILE-18-02-21",
			direction="IMPORT",
			full_name="Agile Octopus February 2018",
			display_name="Agile Octopus",
			description="",
			is_variable=True,
			is_green=True,
			is_tracker=False,
			is_prepay=False,
			is_business=False,
			is_restricted=False,
			term=12,
			available_from="2017-01-01T00:00:00Z",
			available_to=None,
			brand="OCTOPUS_ENERGY",
			links=[{
					"href": "https://api.octopus.energy/v1/products/AGILE-18-02-21/",
					"rel": "self",
					"method": "GET",
					}]
			)

	assert not api.get_products(is_tracker=True)
	assert not api.get_products(is_prepay=True, is_variable=False)


def test_get_product_info(api):
	assert api.get_product_info("VAR-17-01-11") == DetailedProduct(
			code="VAR-17-01-11",
			full_name="Flexible Octopus January 2017 v1",
			display_name="Flexible Octopus",
			description=
			"This variable tariff always offers great value - driven by our belief that prices should be fair for the long term, not just a fixed term. We aim for 50% renewable electricity on this tariff.",
			is_variable=True,
			is_green=False,
			is_tracker=False,
			is_prepay=False,
			is_business=False,
			is_restricted=False,
			term=None,
			available_from="2017-01-11T10:00:00Z",
			available_to="2018-02-15T00:00:00Z",
			tariffs_active_at="2020-09-27T21:12:33.228811Z",
			single_register_electricity_tariffs=single_register_electricity_tariffs,
			dual_register_electricity_tariffs={
					"_A": {
							"direct_debit_monthly": {
									"code": "E-2R-VAR-17-01-11-A",
									"standing_charge_exc_vat": 19.46,
									"standing_charge_inc_vat": 20.433,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-A/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-A/day-unit-rates/",
														"method":
																"GET",
														"rel":
																"day_unit_rates"
														},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-A/night-unit-rates/",
														"method":
																"GET",
														"rel":
																"night_unit_rates"
														}],
									"day_unit_rate_exc_vat": 16.65,
									"day_unit_rate_inc_vat": 17.4825,
									"night_unit_rate_exc_vat": 8.86,
									"night_unit_rate_inc_vat": 9.303
									}
							},
					"_B": {
							"direct_debit_monthly": {
									"code": "E-2R-VAR-17-01-11-B",
									"standing_charge_exc_vat": 18.18,
									"standing_charge_inc_vat": 19.089,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-B/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-B/day-unit-rates/",
														"method":
																"GET",
														"rel":
																"day_unit_rates"
														},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-B/night-unit-rates/",
														"method":
																"GET",
														"rel":
																"night_unit_rates"
														}],
									"day_unit_rate_exc_vat": 15.92,
									"day_unit_rate_inc_vat": 16.716,
									"night_unit_rate_exc_vat": 8.99,
									"night_unit_rate_inc_vat": 9.4395
									}
							},
					"_C": {
							"direct_debit_monthly": {
									"code": "E-2R-VAR-17-01-11-C",
									"standing_charge_exc_vat": 19.11,
									"standing_charge_inc_vat": 20.0655,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-C/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-C/day-unit-rates/",
														"method":
																"GET",
														"rel":
																"day_unit_rates"
														},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-C/night-unit-rates/",
														"method":
																"GET",
														"rel":
																"night_unit_rates"
														}],
									"day_unit_rate_exc_vat": 16.03,
									"day_unit_rate_inc_vat": 16.8315,
									"night_unit_rate_exc_vat": 8.99,
									"night_unit_rate_inc_vat": 9.4395
									}
							},
					"_D": {
							"direct_debit_monthly": {
									"code": "E-2R-VAR-17-01-11-D",
									"standing_charge_exc_vat": 18.61,
									"standing_charge_inc_vat": 19.5405,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-D/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-D/day-unit-rates/",
														"method":
																"GET",
														"rel":
																"day_unit_rates"
														},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-D/night-unit-rates/",
														"method":
																"GET",
														"rel":
																"night_unit_rates"
														}],
									"day_unit_rate_exc_vat": 16.96,
									"day_unit_rate_inc_vat": 17.808,
									"night_unit_rate_exc_vat": 9.5,
									"night_unit_rate_inc_vat": 9.975
									}
							},
					"_E": {
							"direct_debit_monthly": {
									"code": "E-2R-VAR-17-01-11-E",
									"standing_charge_exc_vat": 19.19,
									"standing_charge_inc_vat": 20.1495,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-E/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-E/day-unit-rates/",
														"method":
																"GET",
														"rel":
																"day_unit_rates"
														},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-E/night-unit-rates/",
														"method":
																"GET",
														"rel":
																"night_unit_rates"
														}],
									"day_unit_rate_exc_vat": 16.27,
									"day_unit_rate_inc_vat": 17.0835,
									"night_unit_rate_exc_vat": 8.88,
									"night_unit_rate_inc_vat": 9.324
									}
							},
					"_F": {
							"direct_debit_monthly": {
									"code": "E-2R-VAR-17-01-11-F",
									"standing_charge_exc_vat": 20.35,
									"standing_charge_inc_vat": 21.3675,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-F/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-F/day-unit-rates/",
														"method":
																"GET",
														"rel":
																"day_unit_rates"
														},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-F/night-unit-rates/",
														"method":
																"GET",
														"rel":
																"night_unit_rates"
														}],
									"day_unit_rate_exc_vat": 16.17,
									"day_unit_rate_inc_vat": 16.9785,
									"night_unit_rate_exc_vat": 9.2,
									"night_unit_rate_inc_vat": 9.66
									}
							},
					"_G": {
							"direct_debit_monthly": {
									"code": "E-2R-VAR-17-01-11-G",
									"standing_charge_exc_vat": 18.3,
									"standing_charge_inc_vat": 19.215,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-G/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-G/day-unit-rates/",
														"method":
																"GET",
														"rel":
																"day_unit_rates"
														},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-G/night-unit-rates/",
														"method":
																"GET",
														"rel":
																"night_unit_rates"
														}],
									"day_unit_rate_exc_vat": 16.51,
									"day_unit_rate_inc_vat": 17.3355,
									"night_unit_rate_exc_vat": 9.17,
									"night_unit_rate_inc_vat": 9.6285
									}
							},
					"_H": {
							"direct_debit_monthly": {
									"code": "E-2R-VAR-17-01-11-H",
									"standing_charge_exc_vat": 17.91,
									"standing_charge_inc_vat": 18.8055,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-H/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-H/day-unit-rates/",
														"method":
																"GET",
														"rel":
																"day_unit_rates"
														},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-H/night-unit-rates/",
														"method":
																"GET",
														"rel":
																"night_unit_rates"
														}],
									"day_unit_rate_exc_vat": 16.17,
									"day_unit_rate_inc_vat": 16.9785,
									"night_unit_rate_exc_vat": 9.42,
									"night_unit_rate_inc_vat": 9.891
									}
							},
					"_J": {
							"direct_debit_monthly": {
									"code": "E-2R-VAR-17-01-11-J",
									"standing_charge_exc_vat": 19.4,
									"standing_charge_inc_vat": 20.37,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-J/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-J/day-unit-rates/",
														"method":
																"GET",
														"rel":
																"day_unit_rates"
														},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-J/night-unit-rates/",
														"method":
																"GET",
														"rel":
																"night_unit_rates"
														}],
									"day_unit_rate_exc_vat": 16.9,
									"day_unit_rate_inc_vat": 17.745,
									"night_unit_rate_exc_vat": 9.19,
									"night_unit_rate_inc_vat": 9.6495
									}
							},
					"_K": {
							"direct_debit_monthly": {
									"code": "E-2R-VAR-17-01-11-K",
									"standing_charge_exc_vat": 19.45,
									"standing_charge_inc_vat": 20.4225,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-K/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-K/day-unit-rates/",
														"method":
																"GET",
														"rel":
																"day_unit_rates"
														},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-K/night-unit-rates/",
														"method":
																"GET",
														"rel":
																"night_unit_rates"
														}],
									"day_unit_rate_exc_vat": 16.41,
									"day_unit_rate_inc_vat": 17.2305,
									"night_unit_rate_exc_vat": 9.28,
									"night_unit_rate_inc_vat": 9.744
									}
							},
					"_L": {
							"direct_debit_monthly": {
									"code": "E-2R-VAR-17-01-11-L",
									"standing_charge_exc_vat": 20.13,
									"standing_charge_inc_vat": 21.1365,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-L/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-L/day-unit-rates/",
														"method":
																"GET",
														"rel":
																"day_unit_rates"
														},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-L/night-unit-rates/",
														"method":
																"GET",
														"rel":
																"night_unit_rates"
														}],
									"day_unit_rate_exc_vat": 17.18,
									"day_unit_rate_inc_vat": 18.039,
									"night_unit_rate_exc_vat": 8.93,
									"night_unit_rate_inc_vat": 9.3765
									}
							},
					"_M": {
							"direct_debit_monthly": {
									"code": "E-2R-VAR-17-01-11-M",
									"standing_charge_exc_vat": 20.25,
									"standing_charge_inc_vat": 21.2625,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-M/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-M/day-unit-rates/",
														"method":
																"GET",
														"rel":
																"day_unit_rates"
														},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-M/night-unit-rates/",
														"method":
																"GET",
														"rel":
																"night_unit_rates"
														}],
									"day_unit_rate_exc_vat": 16.04,
									"day_unit_rate_inc_vat": 16.842,
									"night_unit_rate_exc_vat": 9.07,
									"night_unit_rate_inc_vat": 9.5235
									}
							},
					"_N": {
							"direct_debit_monthly": {
									"code": "E-2R-VAR-17-01-11-N",
									"standing_charge_exc_vat": 19.9,
									"standing_charge_inc_vat": 20.895,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-N/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-N/day-unit-rates/",
														"method":
																"GET",
														"rel":
																"day_unit_rates"
														},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-N/night-unit-rates/",
														"method":
																"GET",
														"rel":
																"night_unit_rates"
														}],
									"day_unit_rate_exc_vat": 15.84,
									"day_unit_rate_inc_vat": 16.632,
									"night_unit_rate_exc_vat": 9.31,
									"night_unit_rate_inc_vat": 9.7755
									}
							},
					"_P": {
							"direct_debit_monthly": {
									"code": "E-2R-VAR-17-01-11-P",
									"standing_charge_exc_vat": 22.61,
									"standing_charge_inc_vat": 23.7405,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-P/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-P/day-unit-rates/",
														"method":
																"GET",
														"rel":
																"day_unit_rates"
														},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-2R-VAR-17-01-11-P/night-unit-rates/",
														"method":
																"GET",
														"rel":
																"night_unit_rates"
														}],
									"day_unit_rate_exc_vat": 16.99,
									"day_unit_rate_inc_vat": 17.8395,
									"night_unit_rate_exc_vat": 10.84,
									"night_unit_rate_inc_vat": 11.382
									}
							}
					},
			single_register_gas_tariffs={
					"_A": {
							"direct_debit_monthly": {
									"code": "G-1R-VAR-17-01-11-A",
									"standing_charge_exc_vat": 16.0,
									"standing_charge_inc_vat": 16.8,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-A/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-A/standard-unit-rates/",
														"method":
																"GET",
														"rel":
																"standard_unit_rates"
														}],
									"standard_unit_rate_exc_vat": 3.05,
									"standard_unit_rate_inc_vat": 3.2025
									}
							},
					"_B": {
							"direct_debit_monthly": {
									"code": "G-1R-VAR-17-01-11-B",
									"standing_charge_exc_vat": 16.0,
									"standing_charge_inc_vat": 16.8,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-B/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-B/standard-unit-rates/",
														"method":
																"GET",
														"rel":
																"standard_unit_rates"
														}],
									"standard_unit_rate_exc_vat": 3.06,
									"standard_unit_rate_inc_vat": 3.213
									}
							},
					"_C": {
							"direct_debit_monthly": {
									"code": "G-1R-VAR-17-01-11-C",
									"standing_charge_exc_vat": 16.0,
									"standing_charge_inc_vat": 16.8,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-C/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-C/standard-unit-rates/",
														"method":
																"GET",
														"rel":
																"standard_unit_rates"
														}],
									"standard_unit_rate_exc_vat": 3.3,
									"standard_unit_rate_inc_vat": 3.465
									}
							},
					"_D": {
							"direct_debit_monthly": {
									"code": "G-1R-VAR-17-01-11-D",
									"standing_charge_exc_vat": 16.0,
									"standing_charge_inc_vat": 16.8,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-D/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-D/standard-unit-rates/",
														"method":
																"GET",
														"rel":
																"standard_unit_rates"
														}],
									"standard_unit_rate_exc_vat": 3.26,
									"standard_unit_rate_inc_vat": 3.423
									}
							},
					"_E": {
							"direct_debit_monthly": {
									"code": "G-1R-VAR-17-01-11-E",
									"standing_charge_exc_vat": 16.0,
									"standing_charge_inc_vat": 16.8,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-E/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-E/standard-unit-rates/",
														"method":
																"GET",
														"rel":
																"standard_unit_rates"
														}],
									"standard_unit_rate_exc_vat": 3.15,
									"standard_unit_rate_inc_vat": 3.3075
									}
							},
					"_F": {
							"direct_debit_monthly": {
									"code": "G-1R-VAR-17-01-11-F",
									"standing_charge_exc_vat": 16.0,
									"standing_charge_inc_vat": 16.8,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-F/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-F/standard-unit-rates/",
														"method":
																"GET",
														"rel":
																"standard_unit_rates"
														}],
									"standard_unit_rate_exc_vat": 3.1,
									"standard_unit_rate_inc_vat": 3.255
									}
							},
					"_G": {
							"direct_debit_monthly": {
									"code": "G-1R-VAR-17-01-11-G",
									"standing_charge_exc_vat": 16.0,
									"standing_charge_inc_vat": 16.8,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-G/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-G/standard-unit-rates/",
														"method":
																"GET",
														"rel":
																"standard_unit_rates"
														}],
									"standard_unit_rate_exc_vat": 3.17,
									"standard_unit_rate_inc_vat": 3.3285
									}
							},
					"_H": {
							"direct_debit_monthly": {
									"code": "G-1R-VAR-17-01-11-H",
									"standing_charge_exc_vat": 16.0,
									"standing_charge_inc_vat": 16.8,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-H/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-H/standard-unit-rates/",
														"method":
																"GET",
														"rel":
																"standard_unit_rates"
														}],
									"standard_unit_rate_exc_vat": 3.34,
									"standard_unit_rate_inc_vat": 3.507
									}
							},
					"_J": {
							"direct_debit_monthly": {
									"code": "G-1R-VAR-17-01-11-J",
									"standing_charge_exc_vat": 16.0,
									"standing_charge_inc_vat": 16.8,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-J/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-J/standard-unit-rates/",
														"method":
																"GET",
														"rel":
																"standard_unit_rates"
														}],
									"standard_unit_rate_exc_vat": 3.28,
									"standard_unit_rate_inc_vat": 3.444
									}
							},
					"_K": {
							"direct_debit_monthly": {
									"code": "G-1R-VAR-17-01-11-K",
									"standing_charge_exc_vat": 16.0,
									"standing_charge_inc_vat": 16.8,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-K/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-K/standard-unit-rates/",
														"method":
																"GET",
														"rel":
																"standard_unit_rates"
														}],
									"standard_unit_rate_exc_vat": 3.16,
									"standard_unit_rate_inc_vat": 3.318
									}
							},
					"_L": {
							"direct_debit_monthly": {
									"code": "G-1R-VAR-17-01-11-L",
									"standing_charge_exc_vat": 16.0,
									"standing_charge_inc_vat": 16.8,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-L/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-L/standard-unit-rates/",
														"method":
																"GET",
														"rel":
																"standard_unit_rates"
														}],
									"standard_unit_rate_exc_vat": 3.37,
									"standard_unit_rate_inc_vat": 3.5385
									}
							},
					"_M": {
							"direct_debit_monthly": {
									"code": "G-1R-VAR-17-01-11-M",
									"standing_charge_exc_vat": 16.0,
									"standing_charge_inc_vat": 16.8,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-M/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-M/standard-unit-rates/",
														"method":
																"GET",
														"rel":
																"standard_unit_rates"
														}],
									"standard_unit_rate_exc_vat": 3.12,
									"standard_unit_rate_inc_vat": 3.276
									}
							},
					"_N": {
							"direct_debit_monthly": {
									"code": "G-1R-VAR-17-01-11-N",
									"standing_charge_exc_vat": 16.0,
									"standing_charge_inc_vat": 16.8,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-N/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-N/standard-unit-rates/",
														"method":
																"GET",
														"rel":
																"standard_unit_rates"
														}],
									"standard_unit_rate_exc_vat": 3.11,
									"standard_unit_rate_inc_vat": 3.2655
									}
							},
					"_P": {
							"direct_debit_monthly": {
									"code": "G-1R-VAR-17-01-11-P",
									"standing_charge_exc_vat": 16.0,
									"standing_charge_inc_vat": 16.8,
									"online_discount_exc_vat": 0,
									"online_discount_inc_vat": 0,
									"dual_fuel_discount_exc_vat": 0,
									"dual_fuel_discount_inc_vat": 0,
									"exit_fees_exc_vat": 0,
									"exit_fees_inc_vat": 0,
									"links": [{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-P/standing-charges/",
											"method":
													"GET",
											"rel":
													"standing_charges"
											},
												{
														"href":
																"https://api.octopus.energy/v1/products/VAR-17-01-11/gas-tariffs/G-1R-VAR-17-01-11-P/standard-unit-rates/",
														"method":
																"GET",
														"rel":
																"standard_unit_rates"
														}],
									"standard_unit_rate_exc_vat": 3.1,
									"standard_unit_rate_inc_vat": 3.255
									}
							}
					},
			sample_quotes={
					"_A": {
							"direct_debit_monthly": {
									"electricity_single_rate": {
											"annual_cost_inc_vat": 52080, "annual_cost_exc_vat": 49600
											},
									"electricity_dual_rate": {
											"annual_cost_inc_vat": 66456, "annual_cost_exc_vat": 63291
											},
									"dual_fuel_single_rate": {
											"annual_cost_inc_vat": 96642, "annual_cost_exc_vat": 92040
											},
									"dual_fuel_dual_rate": {
											"annual_cost_inc_vat": 111018, "annual_cost_exc_vat": 105731
											}
									}
							},
					"_B": {
							"direct_debit_monthly": {
									"electricity_single_rate": {
											"annual_cost_inc_vat": 49823, "annual_cost_exc_vat": 47451
											},
									"electricity_dual_rate": {
											"annual_cost_inc_vat": 64339, "annual_cost_exc_vat": 61275
											},
									"dual_fuel_single_rate": {
											"annual_cost_inc_vat": 94511, "annual_cost_exc_vat": 90011
											},
									"dual_fuel_dual_rate": {
											"annual_cost_inc_vat": 109027, "annual_cost_exc_vat": 103835
											}
									}
							},
					"_C": {
							"direct_debit_monthly": {
									"electricity_single_rate": {
											"annual_cost_inc_vat": 50149, "annual_cost_exc_vat": 47761
											},
									"electricity_dual_rate": {
											"annual_cost_inc_vat": 64977, "annual_cost_exc_vat": 61883
											},
									"dual_fuel_single_rate": {
											"annual_cost_inc_vat": 97861, "annual_cost_exc_vat": 93201
											},
									"dual_fuel_dual_rate": {
											"annual_cost_inc_vat": 112689, "annual_cost_exc_vat": 107323
											}
									}
							},
					"_D": {
							"direct_debit_monthly": {
									"electricity_single_rate": {
											"annual_cost_inc_vat": 53307, "annual_cost_exc_vat": 50769
											},
									"electricity_dual_rate": {
											"annual_cost_inc_vat": 68108, "annual_cost_exc_vat": 64865
											},
									"dual_fuel_single_rate": {
											"annual_cost_inc_vat": 100515, "annual_cost_exc_vat": 95729
											},
									"dual_fuel_dual_rate": {
											"annual_cost_inc_vat": 115316, "annual_cost_exc_vat": 109825
											}
									}
							},
					"_E": {
							"direct_debit_monthly": {
									"electricity_single_rate": {
											"annual_cost_inc_vat": 50758, "annual_cost_exc_vat": 48341
											},
									"electricity_dual_rate": {
											"annual_cost_inc_vat": 65418, "annual_cost_exc_vat": 62302
											},
									"dual_fuel_single_rate": {
											"annual_cost_inc_vat": 96580, "annual_cost_exc_vat": 91981
											},
									"dual_fuel_dual_rate": {
											"annual_cost_inc_vat": 111240, "annual_cost_exc_vat": 105942
											}
									}
							},
					"_F": {
							"direct_debit_monthly": {
									"electricity_single_rate": {
											"annual_cost_inc_vat": 51112, "annual_cost_exc_vat": 48678
											},
									"electricity_dual_rate": {
											"annual_cost_inc_vat": 66199, "annual_cost_exc_vat": 63047
											},
									"dual_fuel_single_rate": {
											"annual_cost_inc_vat": 96304, "annual_cost_exc_vat": 91718
											},
									"dual_fuel_dual_rate": {
											"annual_cost_inc_vat": 111391, "annual_cost_exc_vat": 106087
											}
									}
							},
					"_G": {
							"direct_debit_monthly": {
									"electricity_single_rate": {
											"annual_cost_inc_vat": 51148, "annual_cost_exc_vat": 48712
											},
									"electricity_dual_rate": {
											"annual_cost_inc_vat": 66227, "annual_cost_exc_vat": 63074
											},
									"dual_fuel_single_rate": {
											"annual_cost_inc_vat": 97222, "annual_cost_exc_vat": 92592
											},
									"dual_fuel_dual_rate": {
											"annual_cost_inc_vat": 112301, "annual_cost_exc_vat": 106954
											}
									}
							},
					"_H": {
							"direct_debit_monthly": {
									"electricity_single_rate": {
											"annual_cost_inc_vat": 50542, "annual_cost_exc_vat": 48135
											},
									"electricity_dual_rate": {
											"annual_cost_inc_vat": 65671, "annual_cost_exc_vat": 62544
											},
									"dual_fuel_single_rate": {
											"annual_cost_inc_vat": 98758, "annual_cost_exc_vat": 94055
											},
									"dual_fuel_dual_rate": {
											"annual_cost_inc_vat": 113887, "annual_cost_exc_vat": 108464
											}
									}
							},
					"_J": {
							"direct_debit_monthly": {
									"electricity_single_rate": {
											"annual_cost_inc_vat": 52849, "annual_cost_exc_vat": 50332
											},
									"electricity_dual_rate": {
											"annual_cost_inc_vat": 67684, "annual_cost_exc_vat": 64461
											},
									"dual_fuel_single_rate": {
											"annual_cost_inc_vat": 100309, "annual_cost_exc_vat": 95532
											},
									"dual_fuel_dual_rate": {
											"annual_cost_inc_vat": 115144, "annual_cost_exc_vat": 109661
											}
									}
							},
					"_K": {
							"direct_debit_monthly": {
									"electricity_single_rate": {
											"annual_cost_inc_vat": 52320, "annual_cost_exc_vat": 49828
											},
									"electricity_dual_rate": {
											"annual_cost_inc_vat": 66616, "annual_cost_exc_vat": 63444
											},
									"dual_fuel_single_rate": {
											"annual_cost_inc_vat": 98268, "annual_cost_exc_vat": 93588
											},
									"dual_fuel_dual_rate": {
											"annual_cost_inc_vat": 112564, "annual_cost_exc_vat": 107204
											}
									}
							},
					"_L": {
							"direct_debit_monthly": {
									"electricity_single_rate": {
											"annual_cost_inc_vat": 53037, "annual_cost_exc_vat": 50511
											},
									"electricity_dual_rate": {
											"annual_cost_inc_vat": 68198, "annual_cost_exc_vat": 64950
											},
									"dual_fuel_single_rate": {
											"annual_cost_inc_vat": 101631, "annual_cost_exc_vat": 96791
											},
									"dual_fuel_dual_rate": {
											"annual_cost_inc_vat": 116792, "annual_cost_exc_vat": 111230
											}
									}
							},
					"_M": {
							"direct_debit_monthly": {
									"electricity_single_rate": {
											"annual_cost_inc_vat": 50403, "annual_cost_exc_vat": 48003
											},
									"electricity_dual_rate": {
											"annual_cost_inc_vat": 65587, "annual_cost_exc_vat": 62464
											},
									"dual_fuel_single_rate": {
											"annual_cost_inc_vat": 95847, "annual_cost_exc_vat": 91283
											},
									"dual_fuel_dual_rate": {
											"annual_cost_inc_vat": 111031, "annual_cost_exc_vat": 105744
											}
									}
							},
					"_N": {
							"direct_debit_monthly": {
									"electricity_single_rate": {
											"annual_cost_inc_vat": 51000, "annual_cost_exc_vat": 48572
											},
									"electricity_dual_rate": {
											"annual_cost_inc_vat": 65386, "annual_cost_exc_vat": 62273
											},
									"dual_fuel_single_rate": {
											"annual_cost_inc_vat": 96318, "annual_cost_exc_vat": 91732
											},
									"dual_fuel_dual_rate": {
											"annual_cost_inc_vat": 110704, "annual_cost_exc_vat": 105433
											}
									}
							},
					"_P": {
							"direct_debit_monthly": {
									"electricity_single_rate": {
											"annual_cost_inc_vat": 53500, "annual_cost_exc_vat": 50953
											},
									"electricity_dual_rate": {
											"annual_cost_inc_vat": 72200, "annual_cost_exc_vat": 68762
											},
									"dual_fuel_single_rate": {
											"annual_cost_inc_vat": 98692, "annual_cost_exc_vat": 93993
											},
									"dual_fuel_dual_rate": {
											"annual_cost_inc_vat": 117392, "annual_cost_exc_vat": 111802
											}
									}
							}
					},
			sample_consumption={
					"electricity_single_rate": {"electricity_standard": 2900},
					"electricity_dual_rate": {"electricity_day": 2436, "electricity_night": 1764},
					"dual_fuel_single_rate": {"electricity_standard": 2900, "gas_standard": 12000},
					"dual_fuel_dual_rate": {
							"electricity_day": 2436, "electricity_night": 1764, "gas_standard": 12000
							}
					},
			brand="OCTOPUS_ENERGY",
			links=[{
					"href": "https://api.octopus.energy/v1/products/VAR-17-01-11/",
					"rel": "self",
					"method": "GET",
					}]
			)


single_register_electricity_tariffs = {
		"_A": {
				"direct_debit_monthly": {
						"code": "E-1R-VAR-17-01-11-A",
						"standing_charge_exc_vat": 18.46,
						"standing_charge_inc_vat": 19.383,
						"online_discount_exc_vat": 0,
						"online_discount_inc_vat": 0,
						"dual_fuel_discount_exc_vat": 0,
						"dual_fuel_discount_inc_vat": 0,
						"exit_fees_exc_vat": 0,
						"exit_fees_inc_vat": 0,
						"links": [{
								"href":
										"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-A/standing-charges/",
								"method":
										"GET",
								"rel":
										"standing_charges"
								},
									{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-A/standard-unit-rates/",
											"method":
													"GET",
											"rel":
													"standard_unit_rates"
											}],
						"standard_unit_rate_exc_vat": 14.78,
						"standard_unit_rate_inc_vat": 15.519
						}
				},
		"_B": {
				"direct_debit_monthly": {
						"code": "E-1R-VAR-17-01-11-B",
						"standing_charge_exc_vat": 17.18,
						"standing_charge_inc_vat": 18.039,
						"online_discount_exc_vat": 0,
						"online_discount_inc_vat": 0,
						"dual_fuel_discount_exc_vat": 0,
						"dual_fuel_discount_inc_vat": 0,
						"exit_fees_exc_vat": 0,
						"exit_fees_inc_vat": 0,
						"links": [{
								"href":
										"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-B/standing-charges/",
								"method":
										"GET",
								"rel":
										"standing_charges"
								},
									{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-B/standard-unit-rates/",
											"method":
													"GET",
											"rel":
													"standard_unit_rates"
											}],
						"standard_unit_rate_exc_vat": 14.2,
						"standard_unit_rate_inc_vat": 14.91
						}
				},
		"_C": {
				"direct_debit_monthly": {
						"code": "E-1R-VAR-17-01-11-C",
						"standing_charge_exc_vat": 18.11,
						"standing_charge_inc_vat": 19.0155,
						"online_discount_exc_vat": 0,
						"online_discount_inc_vat": 0,
						"dual_fuel_discount_exc_vat": 0,
						"dual_fuel_discount_inc_vat": 0,
						"exit_fees_exc_vat": 0,
						"exit_fees_inc_vat": 0,
						"links": [{
								"href":
										"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-C/standing-charges/",
								"method":
										"GET",
								"rel":
										"standing_charges"
								},
									{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-C/standard-unit-rates/",
											"method":
													"GET",
											"rel":
													"standard_unit_rates"
											}],
						"standard_unit_rate_exc_vat": 14.19,
						"standard_unit_rate_inc_vat": 14.8995
						}
				},
		"_D": {
				"direct_debit_monthly": {
						"code": "E-1R-VAR-17-01-11-D",
						"standing_charge_exc_vat": 17.61,
						"standing_charge_inc_vat": 18.4905,
						"online_discount_exc_vat": 0,
						"online_discount_inc_vat": 0,
						"dual_fuel_discount_exc_vat": 0,
						"dual_fuel_discount_inc_vat": 0,
						"exit_fees_exc_vat": 0,
						"exit_fees_inc_vat": 0,
						"links": [{
								"href":
										"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-D/standing-charges/",
								"method":
										"GET",
								"rel":
										"standing_charges"
								},
									{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-D/standard-unit-rates/",
											"method":
													"GET",
											"rel":
													"standard_unit_rates"
											}],
						"standard_unit_rate_exc_vat": 15.29,
						"standard_unit_rate_inc_vat": 16.0545
						}
				},
		"_E": {
				"direct_debit_monthly": {
						"code": "E-1R-VAR-17-01-11-E",
						"standing_charge_exc_vat": 18.19,
						"standing_charge_inc_vat": 19.0995,
						"online_discount_exc_vat": 0,
						"online_discount_inc_vat": 0,
						"dual_fuel_discount_exc_vat": 0,
						"dual_fuel_discount_inc_vat": 0,
						"exit_fees_exc_vat": 0,
						"exit_fees_inc_vat": 0,
						"links": [{
								"href":
										"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-E/standing-charges/",
								"method":
										"GET",
								"rel":
										"standing_charges"
								},
									{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-E/standard-unit-rates/",
											"method":
													"GET",
											"rel":
													"standard_unit_rates"
											}],
						"standard_unit_rate_exc_vat": 14.38,
						"standard_unit_rate_inc_vat": 15.099
						}
				},
		"_F": {
				"direct_debit_monthly": {
						"code": "E-1R-VAR-17-01-11-F",
						"standing_charge_exc_vat": 19.35,
						"standing_charge_inc_vat": 20.3175,
						"online_discount_exc_vat": 0,
						"online_discount_inc_vat": 0,
						"dual_fuel_discount_exc_vat": 0,
						"dual_fuel_discount_inc_vat": 0,
						"exit_fees_exc_vat": 0,
						"exit_fees_inc_vat": 0,
						"links": [{
								"href":
										"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-F/standing-charges/",
								"method":
										"GET",
								"rel":
										"standing_charges"
								},
									{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-F/standard-unit-rates/",
											"method":
													"GET",
											"rel":
													"standard_unit_rates"
											}],
						"standard_unit_rate_exc_vat": 14.35,
						"standard_unit_rate_inc_vat": 15.0675
						}
				},
		"_G": {
				"direct_debit_monthly": {
						"code": "E-1R-VAR-17-01-11-G",
						"standing_charge_exc_vat": 17.3,
						"standing_charge_inc_vat": 18.165,
						"online_discount_exc_vat": 0,
						"online_discount_inc_vat": 0,
						"dual_fuel_discount_exc_vat": 0,
						"dual_fuel_discount_inc_vat": 0,
						"exit_fees_exc_vat": 0,
						"exit_fees_inc_vat": 0,
						"links": [{
								"href":
										"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-G/standing-charges/",
								"method":
										"GET",
								"rel":
										"standing_charges"
								},
									{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-G/standard-unit-rates/",
											"method":
													"GET",
											"rel":
													"standard_unit_rates"
											}],
						"standard_unit_rate_exc_vat": 14.62,
						"standard_unit_rate_inc_vat": 15.351
						}
				},
		"_H": {
				"direct_debit_monthly": {
						"code": "E-1R-VAR-17-01-11-H",
						"standing_charge_exc_vat": 16.91,
						"standing_charge_inc_vat": 17.7555,
						"online_discount_exc_vat": 0,
						"online_discount_inc_vat": 0,
						"dual_fuel_discount_exc_vat": 0,
						"dual_fuel_discount_inc_vat": 0,
						"exit_fees_exc_vat": 0,
						"exit_fees_inc_vat": 0,
						"links": [{
								"href":
										"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-H/standing-charges/",
								"method":
										"GET",
								"rel":
										"standing_charges"
								},
									{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-H/standard-unit-rates/",
											"method":
													"GET",
											"rel":
													"standard_unit_rates"
											}],
						"standard_unit_rate_exc_vat": 14.47,
						"standard_unit_rate_inc_vat": 15.1935
						}
				},
		"_J": {
				"direct_debit_monthly": {
						"code": "E-1R-VAR-17-01-11-J",
						"standing_charge_exc_vat": 18.4,
						"standing_charge_inc_vat": 19.32,
						"online_discount_exc_vat": 0,
						"online_discount_inc_vat": 0,
						"dual_fuel_discount_exc_vat": 0,
						"dual_fuel_discount_inc_vat": 0,
						"exit_fees_exc_vat": 0,
						"exit_fees_inc_vat": 0,
						"links": [{
								"href":
										"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-J/standing-charges/",
								"method":
										"GET",
								"rel":
										"standing_charges"
								},
									{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-J/standard-unit-rates/",
											"method":
													"GET",
											"rel":
													"standard_unit_rates"
											}],
						"standard_unit_rate_exc_vat": 15.04,
						"standard_unit_rate_inc_vat": 15.792
						}
				},
		"_K": {
				"direct_debit_monthly": {
						"code": "E-1R-VAR-17-01-11-K",
						"standing_charge_exc_vat": 18.45,
						"standing_charge_inc_vat": 19.3725,
						"online_discount_exc_vat": 0,
						"online_discount_inc_vat": 0,
						"dual_fuel_discount_exc_vat": 0,
						"dual_fuel_discount_inc_vat": 0,
						"exit_fees_exc_vat": 0,
						"exit_fees_inc_vat": 0,
						"links": [{
								"href":
										"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-K/standing-charges/",
								"method":
										"GET",
								"rel":
										"standing_charges"
								},
									{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-K/standard-unit-rates/",
											"method":
													"GET",
											"rel":
													"standard_unit_rates"
											}],
						"standard_unit_rate_exc_vat": 14.86,
						"standard_unit_rate_inc_vat": 15.603
						}
				},
		"_L": {
				"direct_debit_monthly": {
						"code": "E-1R-VAR-17-01-11-L",
						"standing_charge_exc_vat": 19.13,
						"standing_charge_inc_vat": 20.0865,
						"online_discount_exc_vat": 0,
						"online_discount_inc_vat": 0,
						"dual_fuel_discount_exc_vat": 0,
						"dual_fuel_discount_inc_vat": 0,
						"exit_fees_exc_vat": 0,
						"exit_fees_inc_vat": 0,
						"links": [{
								"href":
										"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-L/standing-charges/",
								"method":
										"GET",
								"rel":
										"standing_charges"
								},
									{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-L/standard-unit-rates/",
											"method":
													"GET",
											"rel":
													"standard_unit_rates"
											}],
						"standard_unit_rate_exc_vat": 15.01,
						"standard_unit_rate_inc_vat": 15.7605
						}
				},
		"_M": {
				"direct_debit_monthly": {
						"code": "E-1R-VAR-17-01-11-M",
						"standing_charge_exc_vat": 19.25,
						"standing_charge_inc_vat": 20.2125,
						"online_discount_exc_vat": 0,
						"online_discount_inc_vat": 0,
						"dual_fuel_discount_exc_vat": 0,
						"dual_fuel_discount_inc_vat": 0,
						"exit_fees_exc_vat": 0,
						"exit_fees_inc_vat": 0,
						"links": [{
								"href":
										"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-M/standing-charges/",
								"method":
										"GET",
								"rel":
										"standing_charges"
								},
									{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-M/standard-unit-rates/",
											"method":
													"GET",
											"rel":
													"standard_unit_rates"
											}],
						"standard_unit_rate_exc_vat": 14.13,
						"standard_unit_rate_inc_vat": 14.8365
						}
				},
		"_N": {
				"direct_debit_monthly": {
						"code": "E-1R-VAR-17-01-11-N",
						"standing_charge_exc_vat": 18.9,
						"standing_charge_inc_vat": 19.845,
						"online_discount_exc_vat": 0,
						"online_discount_inc_vat": 0,
						"dual_fuel_discount_exc_vat": 0,
						"dual_fuel_discount_inc_vat": 0,
						"exit_fees_exc_vat": 0,
						"exit_fees_inc_vat": 0,
						"links": [{
								"href":
										"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-N/standing-charges/",
								"method":
										"GET",
								"rel":
										"standing_charges"
								},
									{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-N/standard-unit-rates/",
											"method":
													"GET",
											"rel":
													"standard_unit_rates"
											}],
						"standard_unit_rate_exc_vat": 14.37,
						"standard_unit_rate_inc_vat": 15.0885
						}
				},
		"_P": {
				"direct_debit_monthly": {
						"code": "E-1R-VAR-17-01-11-P",
						"standing_charge_exc_vat": 21.61,
						"standing_charge_inc_vat": 22.6905,
						"online_discount_exc_vat": 0,
						"online_discount_inc_vat": 0,
						"dual_fuel_discount_exc_vat": 0,
						"dual_fuel_discount_inc_vat": 0,
						"exit_fees_exc_vat": 0,
						"exit_fees_inc_vat": 0,
						"links": [{
								"href":
										"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-P/standing-charges/",
								"method":
										"GET",
								"rel":
										"standing_charges"
								},
									{
											"href":
													"https://api.octopus.energy/v1/products/VAR-17-01-11/electricity-tariffs/E-1R-VAR-17-01-11-P/standard-unit-rates/",
											"method":
													"GET",
											"rel":
													"standard_unit_rates"
											}],
						"standard_unit_rate_exc_vat": 14.85,
						"standard_unit_rate_inc_vat": 15.5925
						}
				}
		}


def test_parse_tariffs(file_regression: FileRegressionFixture):
	assert isinstance(_parse_tariffs(single_register_electricity_tariffs), RegionalTariffs)
	assert str(_parse_tariffs(single_register_electricity_tariffs)) == "RegionalTariffs(['direct_debit_monthly'])"

	file_regression.check(
			repr(_parse_tariffs(single_register_electricity_tariffs)), encoding="UTF-8", extension=".json"
			)

	tariffs: Dict[str, Dict[str, Tariff]] = {}

	for gsp, payment_methods in single_register_electricity_tariffs.items():
		tariffs[gsp] = {}

		for method, tariff in payment_methods.items():
			tariffs[gsp][method] = Tariff(**tariff)  # type: ignore

	assert repr(_parse_tariffs(single_register_electricity_tariffs)) == str(tariffs)
	assert repr(_parse_tariffs(single_register_electricity_tariffs)) == repr(tariffs)
