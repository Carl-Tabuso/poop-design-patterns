<?php

interface InvoiceStateContract
{
    public function approve(): void;

    public function reject(): void;

    public function void(): void;
}

class BaseInvoiceState implements InvoiceStateContract
{
    public function approve(): void
    {
        throw new Exception('Event invalid for this state.');
    }

    public function reject(): void
    {
        throw new Exception('Event invalid for this state.');
    }

    public function void(): void
    {
        throw new Exception('Event invalid for this state.');
    }
}

class PendingInvoice extends BaseInvoiceState
{
    public function __construct(protected Invoice $invoice) {}

    public function approve(): void
    {
        $nextState = new ApprovedInvoice($this->invoice);

        $this->invoice->setState($nextState);
    }

    public function reject(): void
    {
        $this->invoice->setState(new RejectedInvoice($this->invoice));
    }

    public function void(): void
    {
        $this->invoice->setState(new VoidedInvoice($this->invoice));
    }
}

class ApprovedInvoice extends BaseInvoiceState
{
    public function __construct(protected Invoice $invoice) {}

    public function void(): void
    {
        $this->invoice->setState(new VoidedInvoice($this->invoice));
    }

    public function __toString(): string
    {
        return 'approved invocie';
    }
}

class RejectedInvoice extends BaseInvoiceState
{
    public function __construct(protected Invoice $invoice) {}

    public function void(): void
    {
        $this->invoice->setState(new VoidedInvoice($this->invoice));
    }
}

class VoidedInvoice extends BaseInvoiceState
{
    public function __construct(protected Invoice $invoice) {}
}

final class Invoice
{
    protected InvoiceStateContract $state;

    public function __construct()
    {
        $this->state = new PendingInvoice($this);
    }

    public function setState(InvoiceStateContract $state)
    {
        $this->state = $state;
    }

    public function approve(): void
    {
        $this->state->approve();
    }

    public function reject(): void
    {
        $this->state->reject();
    }

    public function void(): void
    {
        $this->state->void();
    }
}

$invoice = new Invoice();

$invoice->approve();
