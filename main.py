import json

# Costa Rican General Election data for the Legislative Assembly by province.
# Source: Tribunal Supremo de Elecciones (TSE)
election_data: dict[str, dict] = {
    "San José": {
        "seats": 18,
        "results": {
            "Pueblo Soberano": 314_307,  # right/populist
            "Liberación Nacional": 203_357,  # center-left
            "Frente Amplio": 126_419,  # left
            "Coalición Agenda Ciudadana": 40_161,  # center-left
            "Unidad Social Cristiana": 38_313,  # center-right
            "Nueva República": 19_922,  # right
            "Avanza": 16_112,
            "Unidos Podemos": 7_701,
            "Compatriotas": 7_283,
            "Liberal Progresista": 5_706,  # right
            "Progreso Social Democratico": 5_267,  # left
            "Nueva Generación": 3_637,  # right
            "Integracion Nacional": 2_577,
            "Justicia Social Costarricense": 2_371,  # left
            "Centro Democrático y Social": 2_145,
            "De la Clase Trabajadora": 1_817,  # very left
            "Esperanza y Libertad": 1_375,
            "Esperanza Nacional": 1_306,
            "Unión Costarricense Democrática": 1_290,
            "Aquí Costa Rica Manda": 1_037,  # right
            "Anticorrupcion Costarricense": 939,
            "Alianza Costa Rica Primero": 799
        }
    },
    "Cartago": {
        "seats": 6,
        "results": {
            "Pueblo Soberano": 104_267,
            "Liberación Nacional": 84_805,
            "Frente Amplio": 40_718,
            "Coalición Agenda Ciudadana": 16_947,
            "Unidad Social Cristiana": 12_383,
            "Actuemos Ya": 11_577,
            "Unidos Podemos": 6_390,
            "Avanza": 5_160,
            "Nueva República": 4_473,
            "Nueva Generación": 3_051,
            "Progreso Social Democratico": 2_966,
            "Liberal Progresista": 2_346,
            "Justicia Social Costarricense": 1_165,
            "Alianza Costa Rica Primero": 1_089,
            "De la Clase Trabajadora": 986,
            "Integracion Nacional": 937,
            "Centro Democrático y Social": 806,
            "Esperanza y Libertad": 701,
            "Esperanza Nacional": 681,
            "Unión Costarricense Democrática": 499,
            "Aquí Costa Rica Manda": 429
        }
    },
    "Heredia": {
        "seats": 5,
        "results": {
            "Pueblo Soberano": 110_324,
            "Liberación Nacional": 71_733,
            "Frente Amplio": 43_912,
            "Coalición Agenda Ciudadana": 13_153,
            "Unidad Social Cristiana": 9_786,
            "Nueva República": 5_947,
            "Avanza": 5_176,
            "Unidos Podemos": 2_491,
            "Liberal Progresista": 2_299,
            "Progreso Social Democratico": 1_168,
            "Integracion Nacional": 996,
            "Alianza Costa Rica Primero": 959,
            "Centro Democrático y Social": 810,
            "Nueva Generación": 769,
            "Justicia Social Costarricense": 674,
            "De la Clase Trabajadora": 570,
            "Esperanza y Libertad": 554,
            "Esperanza Nacional": 418,
            "Unión Costarricense Democrática": 299,
            "Aquí Costa Rica Manda": 250
        }
    },
    "Alajuela": {
        "seats": 12,
        "results": {
            "Pueblo Soberano": 254_208,
            "Liberación Nacional": 110_207,
            "Frente Amplio": 52_399,
            "Unidad Social Cristiana": 16_628,
            "Coalición Agenda Ciudadana": 12_888,
            "Nueva República": 11_859,
            "Avanza": 7_941,
            "Unidos Podemos": 3_696,
            "Progreso Social Democratico": 3_508,
            "Liberal Progresista": 2_899,
            "Esperanza Nacional": 2_626,
            "Nueva Generación": 2_174,
            "Integracion Nacional": 1_563,
            "Centro Democrático y Social": 1_483,
            "Justicia Social Costarricense": 1_156,
            "De la Clase Trabajadora": 924,
            "Unión Costarricense Democrática": 832,
            "Esperanza y Libertad": 781,
            "Aquí Costa Rica Manda": 717,
            "Alianza Costa Rica Primero": 625
        }
    },
    "Guanacaste": {
        "seats": 5,
        "results": {
            "Pueblo Soberano": 83_052,
            "Liberación Nacional": 30_168,
            "Frente Amplio": 9_430,
            "Unidad Social Cristiana": 9_135,
            "Coalición Agenda Ciudadana": 5_594,
            "Unión Guanacasteca": 5_147,
            "Nueva Generación": 5_050,
            "Nueva República": 4_050,
            "Avanza": 3_403,
            "Unidos Podemos": 1_980,
            "Progreso Social Democratico": 1_667,
            "Liberal Progresista": 1_153,
            "Alianza Costa Rica Primero": 1_015,
            "Integracion Nacional": 557,
            "Justicia Social Costarricense": 536,
            "Centro Democrático y Social": 513,
            "Aquí Costa Rica Manda": 486,
            "Unión Costarricense Democrática": 444,
            "De la Clase Trabajadora": 329,
            "Esperanza y Libertad": 193,
            "Esperanza Nacional": 190
        }
    },
    "Puntarenas": {
        "seats": 6,
        "results": {
            "Pueblo Soberano": 114_410,
            "Liberación Nacional": 30_907,
            "Frente Amplio": 12_061,
            "Unidad Social Cristiana": 10_645,
            "Nueva República": 7_163,
            "Coalición Agenda Ciudadana": 3_809,
            "Progreso Social Democratico": 1_764,
            "Avanza": 1_725,
            "Unidos Podemos": 1_701,
            "Liberal Progresista": 1_661,
            "Alianza Costa Rica Primero": 1_655,
            "Centro Democrático y Social": 1_319,
            "Nueva Generación": 1_164,
            "Integracion Nacional": 730,
            "Espeanza y Libertad": 669,
            "Unión Costarricense Democrática": 642,
            "Justicia Social Costarricense": 561,
            "Aquí Costa Rica Manda": 477,
            "De la Clase Trabajadora": 472,
            "Esperanza Nacional": 464
        }
    },
    "Limón": {
        "seats": 5,
        "results": {
            "Pueblo Soberano": 95_109,
            "Liberación Nacional": 24_443,
            "Unidad Social Cristiana": 12_548,
            "Frente Amplio": 8_143,
            "Nueva República": 5_370,
            "Unidos Podemos": 4_531,
            "Coalición Agenda Ciudadana": 3_802,
            "Justicia Social Costarricense": 2_340,
            "Progreso Social Democratico": 1_924,
            "Avanza": 1_385,
            "Alianza Costa Rica Primero": 1_172,
            "Liberal Progresista": 1_099,
            "Nueva Generación": 1_081,
            "Centro Democrático y Social": 753,
            "Esperanza y Libertad": 718,
            "De la Clase Trabajadora": 465,
            "Integracion Nacional": 445,
            "Unión Costarricense Democrática": 443,
            "Aquí Costa Rica Manda": 432,
            "Esperanza Nacional": 376
        }
    },
}

def filter_votes(results: dict[str, int], threshold: int|float):
    """Filters results by subquotient threshold as defined by Costa Rican law."""
    pass_filter = {}
    fail_filter = {}
    for party, vote_count in results.items():
        if vote_count >= threshold:
            pass_filter[party] = vote_count
        else:
            fail_filter[party] = vote_count
    return {"pass": pass_filter, "fail": fail_filter}


def allot_seats(seats: int, results: dict[str, int]):
    """Calculates allocated seats using quotient and remainder metrics."""
    total = sum(results.values())
    if total == 0 or seats == 0:
        return {}
    
    quotient = total / seats
    subquotient = quotient / 2

    # Parties must cross the subquotient threshold to participate in allotment
    filtered = filter_votes(results, subquotient)
    remaining_votes = filtered["pass"]

    # Allot whole numbers of seats based on the quotient
    seat_allocation = {
        party: int(vote_count // quotient)
        for party, vote_count in remaining_votes.items()
    }
    
    # Calculate leftovers (remainders)
    remaining_votes = {
        party: vote_count % quotient
        for party, vote_count in remaining_votes.items()
    }

    # Distribute left-over seats by greatest remainder
    unallocated_seats = seats - sum(seat_allocation.values())

    used_remainders = {}
    while unallocated_seats > 0 and remaining_votes:
        highest_remainder = max(
            remaining_votes,
            key=lambda p: (remaining_votes[p], seat_allocation.get(p, 0) > 0)
        )
        seat_allocation[highest_remainder] = seat_allocation.get(highest_remainder, 0) + 1
        unallocated_seats -= 1
        used_remainders[highest_remainder] = remaining_votes.pop(highest_remainder)
        
        if not remaining_votes and unallocated_seats > 0:
            remaining_votes = used_remainders.copy()

    # Clean up parties with 0 seats
    return {party: seats for party, seats in seat_allocation.items() if seats > 0}


def calculate_national_seats(election_data: dict[str, dict]):
    """Aggregates calculated seat allocations from all provinces."""
    national_results = {}
    for provincia, data in election_data.items():
        province_results = allot_seats(data["seats"], data["results"])
        for party, seats in province_results.items():
            national_results[party] = national_results.get(party, 0) + seats
    return national_results


def generate_web_payload(election_data: dict[str, dict]):
    """
    Processes election data, calculates seat distribution, compiles popular vote 
    shares, and packages them dynamically into the structured dashboard JSON.
    """
    # 1. First, calculate seats for all parties
    national_seats = calculate_national_seats(election_data)
    
    # 2. Identify "major parties" (any party that won at least 1 seat nationally)
    major_parties = {party for party, seats in national_seats.items() if seats > 0}
    
    # 3. Compute national vote sums for calculating accurate popular vote %
    national_vote_sums = {}
    total_national_votes = 0
    for provincia, data in election_data.items():
        for party, votes in data["results"].items():
            national_vote_sums[party] = national_vote_sums.get(party, 0) + votes
            total_national_votes += votes

    # Compile National Seat & Popular Vote metrics
    processed_national_seats = {}
    processed_national_votes = {}
    
    other_seats = 0
    other_votes = 0

    for party, seats in national_seats.items():
        if party in major_parties:
            processed_national_seats[party] = seats
        else:
            other_seats += seats

    for party, votes in national_vote_sums.items():
        percentage = (votes / total_national_votes) * 100 if total_national_votes > 0 else 0
        if party in major_parties:
            processed_national_votes[party] = round(percentage, 2)
        else:
            other_votes += percentage

    if other_seats > 0:
        processed_national_seats["Other"] = other_seats
    processed_national_votes["Other"] = round(other_votes, 2)

    payload = {
        "national_total": {
            "seats": processed_national_seats,
            "popular_vote": processed_national_votes
        },
        "provinces": {}
    }

    # Compile Provincial Seat & Popular Vote metrics
    for provincia, data in election_data.items():
        province_seats = allot_seats(data["seats"], data["results"])
        province_votes_raw = data["results"]
        total_provincial_votes = sum(province_votes_raw.values())

        prov_seats_processed = {}
        prov_votes_processed = {}
        prov_other_seats = 0
        prov_other_votes = 0

        # Map seats
        for party, seats in province_seats.items():
            if party in major_parties:
                prov_seats_processed[party] = seats
            else:
                prov_other_seats += seats

        # Map votes
        for party, votes in province_votes_raw.items():
            percentage = (votes / total_provincial_votes) * 100 if total_provincial_votes > 0 else 0
            if party in major_parties:
                prov_votes_processed[party] = round(percentage, 2)
            else:
                prov_other_votes += percentage

        if prov_other_seats > 0:
            prov_seats_processed["Other"] = prov_other_seats
        prov_votes_processed["Other"] = round(prov_other_votes, 2)

        payload["provinces"][provincia] = {
            "total_seats_available": data["seats"],
            "seats": prov_seats_processed,
            "popular_vote": prov_votes_processed
        }

    return payload


if __name__ == "__main__":
    web_data = generate_web_payload(election_data)
    
    # Save directly to JSON for immediate web ingestion
    output_filename = 'election_results.json'
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(web_data, f, ensure_ascii=False, indent=2)
        
    print(f"\n[Success] Calculated seat allotment & compiled vote ratios successfully!")
    print(f"[Success] Generated dashboard database: '{output_filename}'\n")

    # Output Console summary of National Seats for reference
    print("--- Calculated National Seats Summary ---")
    for party, seats in sorted(web_data["national_total"]["seats"].items(), key=lambda x: x[1], reverse=True):
        print(f" * {party}: {seats} seats")


""" Summary of Changes:
1. **Dynamic Identification of Major Parties**: The script automatically detects which parties won $\ge 1$ seat nationally and preserves their individual categories.
2. **Aggregating Smaller Parties into `"Other"`**: All minor parties that did not secure seats have their popular vote shares and seats automatically calculated, summed up, and grouped under the `"Other"` label.
3. **Structured JSON Output**: The payload structure matches both the `seats` and `popular_vote` requirements used directly by the map frontend (`index.html`).
4. **Automated Writing File**: It automatically outputs `election_results.json` directly to your folder upon executing the Python script.
"""