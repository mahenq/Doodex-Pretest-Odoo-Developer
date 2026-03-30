package main

import "time"

type Status string

const (
	StatusSuccess Status = "SUCCESS"
	StatusFailed  Status = "FAILED"
	StatusPending Status = "PENDING"
)

type DiscountTier string

const (
	TierSuperVIP DiscountTier = "SUPER_VIP"
	TierPremium  DiscountTier = "PREMIUM"
	TierRegular  DiscountTier = "REGULAR"
	TierNone     DiscountTier = "NONE"
)

const (
	thresholdSuperVIP = 50
	thresholdPremium  = 20
	thresholdRegular  = 10

	pointsHighValue    = 5
	pointsWeekend      = 3
	minHighValueAmount = 500_000.0
)

type Transaction struct {
	ID     string
	Amount float64
	Date   time.Time
	Status Status
}

type LoyaltyResult struct {
	TotalPoints               int
	MaxDiscount               DiscountTier
	HighValueTransactionCount int
}

type DiscountInfo struct {
	Tier       DiscountTier
	Percentage int
}

var DiscountTable = []DiscountInfo{
	{TierSuperVIP, 20},
	{TierPremium, 10},
	{TierRegular, 5},
	{TierNone, 0},
}

// Fungsi utama

func CalculateLoyalty(transactions []Transaction) LoyaltyResult {
	var totalPoints, highValueCount int

	for _, tx := range transactions {
		if tx.Status == StatusFailed {
			continue
		}

		points := pointsForTransaction(tx)
		totalPoints += points

		if tx.Amount >= minHighValueAmount {
			highValueCount++
		}
	}

	return LoyaltyResult{
		TotalPoints:               totalPoints,
		MaxDiscount:               discountTier(totalPoints),
		HighValueTransactionCount: highValueCount,
	}
}

func pointsForTransaction(tx Transaction) int {
	isHighValue := tx.Amount >= minHighValueAmount
	isWeekend := isWeekendDay(tx.Date)

	switch {
	case isHighValue:
		return pointsHighValue
	case isWeekend:
		return pointsWeekend
	default:
		return 0
	}
}

func isWeekendDay(t time.Time) bool {
	wd := t.Weekday()
	return wd == time.Saturday || wd == time.Sunday
}

func discountTier(points int) DiscountTier {
	switch {
	case points >= thresholdSuperVIP:
		return TierSuperVIP
	case points >= thresholdPremium:
		return TierPremium
	case points >= thresholdRegular:
		return TierRegular
	default:
		return TierNone
	}
}

func DiscountPercentage(tier DiscountTier) int {
	for _, d := range DiscountTable {
		if d.Tier == tier {
			return d.Percentage
		}
	}
	return 0
}
